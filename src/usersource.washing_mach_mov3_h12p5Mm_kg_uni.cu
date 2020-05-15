

__device__ __host__
int addsourceterms2_MODID(real *dw, real *wd, real *w, struct params *p, struct state *s,int *ii,int field,int dir) {

  int direction;
  int status=0;

   real xc1,xc2,xc3;
   real xxmax,yymax;
   real dx,dy,dz;
   real aa;
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
    aa=0.1;
    //aa=0.01;
    s_period=180.0;
    tdep=1.00;

   xc2_i=0.3e6;

   // xc2_i=0.0;
    xc3_i=1.55e6;

    //xc2_i=1.0e6;
    //xc3_i=1.0e6;




    xc2_0=1.25e6;
    xc3_0=1.25e6;
    t0=s_period;


     xc1=0.5e6;
    xc2=1.27e6;
    xc3=1.27e6;

    xc2=xc2_0+(qt-t0)*(xc2_0-xc2_i)/t0;
    xc3=xc3_i+(qt-t0)*(xc3_0-xc3_i)/t0;

        //  xp=(p->xmin[1])+(((real)j)*(p->dx[1]))-xc2;
        //  zp=(p->xmin[0])+(((real)i)*(p->dx[0]))-xc1;
        //  yp=(p->xmin[2])+(((real)k)*(p->dx[2]))-xc3;
     // xx=x(ix_1,ix_2,ix_3,2)-xc2
     // yy=x(ix_1,ix_2,ix_3,3)-xc3
     // zz=x(ix_1,ix_2,ix_3,1)-xc1  


          xp=wd[fencode3_MODID(p,ii,pos2)]-xc2;
          zp=wd[fencode3_MODID(p,ii,pos1)]-xc1;
          yp=wd[fencode3_MODID(p,ii,pos3)]-xc3;  
     

    //xc2=xc2_0+(qt-t0)*(xc2_0-xc2_i)/t0;
    //xc3=xc3_i+(qt-t0)*(xc3_0-xc3_i)/t0;


    xxmax=2.54e6;
    yymax=2.54e6;

    //dx=p->dx[1];
    //dy=p->dx[2];
    //dz=p->dx[0];


    //dx=0.1e6;
    //dy=0.1e6;
    //dz=0.05e6;


    dx=0.125e6;
    dy=0.125e6;
    dz=0.125e6;
   


    
    

        //exp_z=exp(-zz**2.d0/(delta_z**2.d0))
        //exp_x=exp(-xx**2.d0/(delta_x**2.d0))
        //exp_y=exp(-yy**2.d0/(delta_y**2.d0))       
        //exp_xyz=exp_x*exp_y*exp_z
        exp_z=exp(-zp*zp/(dz*dz));
        exp_x=exp(-xp*xp/(dx*dx));
        exp_y=exp(-yp*yp/(dy*dy));       
        exp_xyz=exp_x*exp_y*exp_z;

        //vvx(ix_1,ix_2,ix_3)=AA*yy/yymax*exp_xyz*tdep    
        //vvy(ix_1,ix_2,ix_3)=-AA*xx/xxmax*exp_xyz*tdep 

        //torsional driver
        //vx=(aa*yp/yymax)*exp_xyz*tdep;    
        //vy=-(aa*xp/xxmax)*exp_xyz*tdep;


       //washing machine driver
       // tdepx=sin(qt*2.0*PI/s_period);
       // tdepy=sin((qt-(0.25*s_period))*2.0*PI/s_period);
       // tdec=(qt<t0?exp(-(qt-t0)*(qt-t0)/(t0*t0)):1);
        //aa=aa*exp(-(qt-582)/90); //amplitude decay after 582s
        aa=aa*tdep*exp_xyz;
       // vx=aa*exp_xyz*tdepx;    
      //  vy=aa*exp_xyz*tdepy;


       mvx=w[fencode3_MODID(p,ii,mom1)];
       mvy=w[fencode3_MODID(p,ii,mom2)];
       mvz=w[fencode3_MODID(p,ii,mom3)];

 	w[fencode3_MODID(p,ii,rho)]+=(p->dt)*aa*w[fencode3_MODID(p,ii,rhob)];
       w[fencode3_MODID(p,ii,energy)]+=0.5*(p->dt)*(mvx*mvx+mvy*mvy+mvz*mvz)/(w[fencode3_MODID(p,ii,rho)]+w[fencode3_MODID(p,ii,rhob)]);


                        //   w[fencode3_MODID(p,ii,mom2)]+=(p->dt)*vx*(w[fencode3_MODID(p,ii,rho)]+w[fencode3_MODID(p,ii,rhob)]);
  
                         //  w[fencode3_MODID(p,ii,mom3)]+=(p->dt)*vy*(w[fencode3_MODID(p,ii,rho)]+w[fencode3_MODID(p,ii,rhob)]);

                        //  w[fencode3_MODID(p,ii,energy)]+=(p->dt)*(vx*vx+vy*vy)*(w[fencode3_MODID(p,ii,rho)]+w[fencode3_MODID(p,ii,rhob)])/2.0;

        //if(i==9  && k==64 )  
        // if(i==9 && j==63 && k==63  )      
       // if(i==9 && j==63 && k==63 && ((p->it)%1000)==0 )
       // if(i==9 && j>61 && j<64 && k>61 && k<64 )
      //  if(i>0 && i<10 && k>60 && k<65 && j>=0 && j<15 && ((p->it)%10)==0) 
	//{
               // p->test=(w[fencode3_MODID(p,ii,energy)]);
               // p->chyp[0]=(w[fencode3_MODID(p,ii,mom2)]);
               // p->chyp[1]=(w[fencode3_MODID(p,ii,mom3)]);


              // printf("%d %d %d %d %f %f %f %f %f %f\n",p->it,i,j,k,qt,tdepx,tdepy,exp_xyz,vx,vy); 
             //printf("source %d %d %d %d %f %f %f %f  %f %f\n",p->it,i,j,k,qt,aa,exp_xyz,tdep,xc2,xc3); 

	//}

  return ( status);
}

__device__ __host__
int addsourceterms1_MODID(real *dw, real *wd, real *w, struct params *p, struct state *s,int *ii,int field,int dir) {


}

