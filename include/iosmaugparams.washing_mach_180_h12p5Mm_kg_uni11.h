


real g  = 9.81;
real u0 = 0;                               
real v0 = 0;
real b0  = 0;                               
real h0 = 5030; 

real cmax[NDIM];
real courantmax;

int ngi=2;
int ngj=2;
int ngk=2;



//Domain definition
// Define the x domain


//#ifdef USE_SAC
int ni;
ni=124; //BW tests
//ni=252;//2d model
ni=ni+2*ngi;
//ni=512;
//real xmax = 6.2831853;  


real xmax=12.8496e6;
//real xmin=199219.0;
real xmin=205700.0;
real dx = (xmax-xmin)/(ni-2*ngi);
//#endif



// Define the y domain



int nj=124;  //BW test
//nj=252;//2d model
nj=nj+2*ngj;
//nj=512;
//real ymax = 6.2831853; 
real ymax=2.56e6;
real ymin=40980.0;

//real dx = xmax/(ni-4);
real dy = (ymax-ymin)/(nj-2*ngj);  
//nj=41;


               

#ifdef USE_SAC_3D

int nk;
nk=124;    //BW tests

nk=nk+2*ngk;
real zmax=2.56e6;
real zmin=40980.0;

//real dx = xmax/(ni-4);
real dz = (zmax-zmin)/(nk-2*ngk);
#endif  



//printf("dx %f %f %f\n",dx,dy,dz);   
real *x=(real *)calloc(ni,sizeof(real));
for(i=0;i<ni;i++)
		x[i]=(xmin-ngi*dx)+i*dx;

real *y=(real *)calloc(nj,sizeof(real));
for(i=0;i<nj;i++)
		y[i]=(ymin-ngj*dy)+i*dy;


real *z=(real *)calloc(nk,sizeof(real));
for(i=0;i<nk;i++)
		z[i]=(zmin-ngk*dz)+i*dz;

int step=0;
//real tmax = 200;
real tmax = 0.2;
int steeringenabled=1;
int finishsteering=0;
char configfile[300];
//char *cfgfile="zero1.ini";
//char *cfgfile="3D_128_128_128_asc_50.ini";
//char *cfgfile="3D_tubeact_128_128_128_asc_50.ini";
//char *cfgfile="configs/3D_tubeact_128_128_128_asc_50.ini";
//char *cfgfile="configs/3D_10_10_6_tube_asc.ini";
//char *cfgfile="configs/spruit_const_asc.ini";
//char *cfgfile="configs/3D_10_10_6_asc.ini";
char *cfgfile="/fastdata/cs1mkg/smaug_wash/washmc_2p5_2p5_12p5_mach180_uni11/washmc_asc_540000.ini";
//char *cfgfile="/fastdata/cs1mkg/smaug/washing_mach/washmc_asc_499000.ini";


//char *cfgfile="configs/3D_128_2p5_2p5_12p5_p0375T_asc_udvmft.ini";
//char *cfgfile="zero1_BW_bin.ini";
//char *cfgout="3D_tube_128_128_128";
//char *cfgout="/fastdata/cs1mkg/sac_cuda/out_ndriver_nohyp_npgft/3D_tube_128_128_128";
//char *cfgout="/fastdata/cs1mkg/sac_cuda/out_driver_hyp_tube/3D_atubet1slow_128_128_128_final";
//char *cfgout="/fastdata/cs1mkg/smaug/washmc_10_10_6_180/washmc_";
//char *cfgout="/fastdata/cs1mkg/smaug/washmc_2p5_2p5_12p5_180_kg/washmc_";

//used for initiali configuration
//char *cfgout="configs/3D_10_10_6_tube_bin.ini";
char *cfgout="/fastdata/cs1mkg/smaug_wash/washmc_2p5_2p5_12p5_mach180_uni11/washmc_";


struct params *d_p;
struct params *p=(struct params *)malloc(sizeof(struct params));

struct state *d_state;
struct state *state=(struct state *)malloc(sizeof(struct state));

#ifdef USE_SAC
dt=2.0;  //bach test

#endif

#ifdef USE_SAC_3D
//dt=2.0;  //BACH3D
//dt=0.13;  //BACH3D
dt=0.001;  //BACH3D
#endif


/*//dt=0.15;

//#ifdef USE_SAC
//dt=0.00065;  //OZT test
//dt=6.5/10000000.0; //BW test
//dt=0.00000065;  //BW tests
dt=0.000000493;  //BW tests
//dt=0.005;
//dt=0.000139;
//dt=3.0/10000000.0; //BW test
//#endif*/


int nt=(int)((tmax)/dt);
//nt=3000;
//nt=5000000;
nt=2000000;
nt=2000000;
//nt=21;
real *t=(real *)calloc(nt,sizeof(real));
printf("runsim 1%d \n",nt);
//t = [0:dt:tdomain];
for(i=0;i<nt;i++)
		t[i]=i*dt;

p->qt=540.0;
p->it=540000;

//p->qt=0;
//p->it=0;


//real courant = wavespeed*dt/dx;

p->n[0]=ni;
p->n[1]=nj;
p->ng[0]=ngi;
p->ng[1]=ngj;

p->npgp[0]=1;
p->npgp[1]=1;

#ifdef USE_SAC_3D
p->n[2]=nk;
p->ng[2]=ngk;
p->npgp[2]=1;
#endif

p->dt=dt;
p->dx[0]=dx;
p->dx[1]=dy;

#ifdef USE_SAC_3D
p->dx[2]=dz;
#endif
//p->g=g;



/*constants used for adiabatic hydrodynamics*/
/*
p->gamma=2.0;
p->adiab=0.5;
*/

p->gamma=1.66666667;






p->mu=1.0;
p->eta=0.0;
//p->g[0]=-274.0;
p->g[0]=0.0;
p->g[1]=0.0;
p->g[2]=0.0;
#ifdef USE_SAC_3D

#endif
//p->cmax=1.0;
p->cmax=0.02;
p->courant=0.2;
p->rkon=0.0;
p->sodifon=0.0;
p->moddton=0.0;
p->divbon=0.0;
p->divbfix=0.0;
p->hyperdifmom=1.0;
p->readini=1.0;
p->cfgsavefrequency=1000;


p->xmax[0]=xmax;
p->xmax[1]=ymax;
p->xmin[0]=xmin;
p->xmin[1]=ymin;
#ifdef USE_SAC_3D
p->xmax[2]=zmax;
p->xmin[2]=zmin;
#endif

p->nt=nt;
p->tmax=tmax;

p->steeringenabled=steeringenabled;
p->finishsteering=finishsteering;

p->maxviscoef=0;
//p->chyp=0.0;       
//p->chyp=0.00000;
p->chyp3=0.00000;


for(i=0;i<NVAR;i++)
  p->chyp[i]=0.0;

p->chyp[rho]=0.02;
p->chyp[energy]=0.02;
p->chyp[b1]=0.02;
p->chyp[b2]=0.02;
p->chyp[mom1]=0.4;
p->chyp[mom2]=0.4;

p->chyp[rho]=0.02;
p->chyp[mom1]=0;
p->chyp[mom2]=0;





p->chyp[rho]=0.02;
p->chyp[energy]=0.02;
p->chyp[b1]=0.02;
p->chyp[b2]=0.02;
p->chyp[mom1]=0.4;
p->chyp[mom2]=0.4;
#ifdef USE_SAC_3D
p->chyp[mom3]=0.4;
p->chyp[b3]=0.02;
#endif



iome elist;
meta meta;


//set boundary types
for(int ii=0;ii<NVAR; ii++)
for(int idir=0; idir<NDIM; idir++)
for(int ibound=0; ibound<2; ibound++)
{
   (p->boundtype[ii][idir][ibound])=4;  //period=0 mpi=1 mpiperiod=2  cont=3 contcd4=4 fixed=5 symm=6 asymm=7
}

//set boundary types
for(int ii=0;ii<NVAR; ii++)
for(int ibound=0; ibound<2; ibound++)
{
   (p->boundtype[ii][0][ibound])=4;  //period=0 mpi=1 mpiperiod=2  cont=3 contcd4=4 fixed=5 symm=6 asymm=7
}


elist.server=(char *)calloc(500,sizeof(char));


meta.directory=(char *)calloc(500,sizeof(char));
meta.author=(char *)calloc(500,sizeof(char));
meta.sdate=(char *)calloc(500,sizeof(char));
meta.platform=(char *)calloc(500,sizeof(char));
meta.desc=(char *)calloc(500,sizeof(char));
meta.name=(char *)calloc(500,sizeof(char));
meta.ini_file=(char *)calloc(500,sizeof(char));
meta.log_file=(char *)calloc(500,sizeof(char));
meta.out_file=(char *)calloc(500,sizeof(char));

strcpy(meta.directory,"out");
strcpy(meta.author,"MikeG");
strcpy(meta.sdate,"Nov 2009");
strcpy(meta.platform,"swat");
strcpy(meta.desc,"A simple test of SAAS");
strcpy(meta.name,"test1");
strcpy(meta.ini_file,"test1.ini");
strcpy(meta.log_file,"test1.log");
strcpy(meta.out_file,"test1.out");
//meta.directory="out";
//meta.author="MikeG";
//meta.sdate="Nov 2009";
//meta.platform="felix";
//meta.desc="A simple test of SAAS";
//meta.name="tsteer1";

	strcpy(elist.server,"localhost1");
	elist.port=80801;
	elist.id=0;

