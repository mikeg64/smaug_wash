  //Number threads per block
  int NTPB=512;
  //Num blocks is determined by size of zeropadded 2^n size array
  int numBlocks = (ndimp+NTPB-1) / NTPB;
  //Shared memory
  int smemSize = NTPB * sizeof(double);
  //Array to store maximum values for reduction in host memory 
  double *h_cmax = (double*)malloc(numBlocks*sizeof(double));

  cudaMalloc((void**)&d_cmax, numBlocks*sizeof(double));
  //Array to store maximum values for reduction in GPU global memory 
  cudaMalloc((void**)&d_bmax, numBlocks*sizeof(double)); 
  
  //set maximum value to zero and update values in GPU memory
  (*p)->cmax=0.0;
  cudaMemcpy(*d_p, *p, sizeof(struct params), cudaMemcpyHostToDevice);
 
  //copy speeds and temporary values to device memory 
  copytotemp_parallel<<<numBlocks, numThreadsPerBlock>>>(*d_p, *d_wd, *d_wtemp,cfast);
  int i=0;

  //find the maximum in each block
  for(i=0;i<numBlocks;i++)
                h_cmax[i]=0;
  cudaMemcpy(d_bmax, h_cmax, numBlocks*sizeof(double), cudaMemcpyHostToDevice);

  reductionmax_parallel<<<numBlocks,NTPB,smemSize>>>(d_bmax,*d_wtemp,ndimp);
  cudaThreadSynchronize();
  cudaMemcpy(h_cmax, d_bmax, numBlocks*sizeof(double), cudaMemcpyDeviceToHost);

  //compare the maxima for all of the blocks and determine maximum value
  for( i=0;i<numBlocks;i++)          		
                if(h_cmax[i]>((*p)->cmax)) ((*p)->cmax)=h_cmax[i];


 //determine maximum value
 cudaMemcpy(*d_wtemp, ((*wd)+(soundspeed*dimp)), dimp*sizeof(real), cudaMemcpyHostToDevice);
