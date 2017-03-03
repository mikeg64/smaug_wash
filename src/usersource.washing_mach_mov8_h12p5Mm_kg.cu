

__device__ __host__
int addsourceterms2_MODID(real *dw, real *wd, real *w, struct params *p, struct state *s,int *ii,int field,int dir) {

  int direction;
  int status=0;

   real xc1,xc2,xc3;
   real xxmax,yymax;
   real dx,dy,dz;
   real aa, av;
   real s_period;
   real qt,tdep,tdepx,tdepy;

   real vx,vy,vz;
   real mvx, mvy, mvz;

   real exp_x,exp_y,exp_z,exp_xyz;
   real xc2_i,xc2_0,xc3_i,xc3_0;
   real tdec,t0;

   real xp,yp,zp;
   int i,j,k;
 	  
	  i=ii[0];
	  j=ii[1];
	  k=ii[2];

   qt=p->qt;
   //aa=0.005;
   //av=50.0;
   aa=0.01;
   av=10000.0;
 

   //xc2_i=0.6e6;  //y-dist
   xc2_i=1.0e6;  //y-dist

   // xc2_i=0.0;
  //  xc3_i=1.0e6;  //x-dist
   xc3_i=1.0e6;  //x-dist

    //xc2_i=1.0e6;
    //xc3_i=1.0e6;




    xc2_0=1.25e6;
    xc3_0=1.25e6;
 

     xc1=0.5e6;
    xc2=xc2_i;
    xc3=xc3_i;

 


          xp=wd[fencode3_MODID(p,ii,pos2)]-xc2;
          zp=wd[fencode3_MODID(p,ii,pos1)]-xc1;
          yp=wd[fencode3_MODID(p,ii,pos3)]-xc3;  
     

    xxmax=2.54e6;
    yymax=2.54e6;

    //dx=p->dx[1];
    //dy=p->dx[2];
    //dz=p->dx[0];


    //dx=0.1e6;
    //dy=0.1e6;
    //dz=0.05e6;


    //dx=0.125e6;
    //dy=0.125e6;
   // dz=0.125e6;
   

    dx=0.0625e6;
    dy=0.0625e6;
    dz=0.0625e6;

    
    

        //exp_z=exp(-zz**2.d0/(delta_z**2.d0))
        //exp_x=exp(-xx**2.d0/(delta_x**2.d0))
        //exp_y=exp(-yy**2.d0/(delta_y**2.d0))       
        //exp_xyz=exp_x*exp_y*exp_z
        exp_z=exp(-zp*zp/(dz*dz));
        exp_x=exp(-xp*xp/(dx*dx));
        exp_y=exp(-yp*yp/(dy*dy));       
        exp_xyz=exp_x*exp_y*exp_z;



       //washing machine driver
        aa=aa*exp_xyz;
        av=av*exp_xyz;
       // vx=aa*exp_xyz*tdepx;    
      //  vy=aa*exp_xyz*tdepy;

        w[fencode3_MODID(p,ii,rho)]+=aa*w[fencode3_MODID(p,ii,rhob)];
       w[fencode3_MODID(p,ii,mom2)]+=av*(w[fencode3_MODID(p,ii,rhob)]+w[fencode3_MODID(p,ii,rho)]);

       mvx=w[fencode3_MODID(p,ii,mom1)];
       mvy=w[fencode3_MODID(p,ii,mom2)];
       mvz=w[fencode3_MODID(p,ii,mom3)];

 	
       w[fencode3_MODID(p,ii,energy)]+=0.5*(mvx*mvx+mvy*mvy+mvz*mvz)/(w[fencode3_MODID(p,ii,rho)]+w[fencode3_MODID(p,ii,rhob)]);

       // if(i==9 && j==63 && k==63 && ((p->it)%1000)==0 )
        //if(i==9 && j>61 && j<64 && k>61 && k<64 )
      //  if(i>0 && i<10 && k>60 && k<65 && j>=0 && j<15 && ((p->it)%10)==0) 
	//{
               // p->test=(w[fencode3_MODID(p,ii,energy)]);
               // p->chyp[0]=(w[fencode3_MODID(p,ii,mom2)]);
               // p->chyp[1]=(w[fencode3_MODID(p,ii,mom3)]);


              // printf("%d %d %d %d %f %f %f %f %f %f\n",p->it,i,j,k,qt,tdepx,tdepy,exp_xyz,vx,vy); 
            // printf("%d %d %d %d %f %f %f %f \n",p->it,i,j,k,qt,aa,exp_xyz,tdep); 

	//}

  return ( status);
}

__device__ __host__
int addsourceterms1_MODID(real *dw, real *wd, real *w, struct params *p, struct state *s,int *ii,int field,int dir) {


}

