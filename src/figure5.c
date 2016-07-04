  extern __shared__ double partialResult[];

  int i;
   partialResult[tid]=0.0;
   if(iindex<ndimp)
              partialResult[tid]=temp[iindex];
  __syncthreads();


for(unsigned int s=1; s < blockDim.x; s *= 2) {
        if ((tid % (2*s)) == 0) {
            if(partialResult[tid+s]>partialResult[tid])
                 partialResult[tid]=partialResult[tid + s];
        }
        __syncthreads();
    }

    __syncthreads();
    if(tid==0)
    {
      cmax[blockIdx.x]=partialResult[0];
      //temp[blockIdx.x]=partialResult[0];
     }
     __syncthreads();