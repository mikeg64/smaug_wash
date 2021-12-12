% compute the ampitude ratios
%see note .  https://community.researchspace.com/notebookEditor/1428875?initialRecordToDisplay=1428876&settingsKey=gEbpzzwlHn
%
% as described in
%
% https://ui.adsabs.harvard.edu/abs/2013A%26A...551A.137M/abstract
%

directory='/shared/sp2rc2/Shared/simulations/smaug_realpmode/fastdata/cs1mkg/smaug/spic_5b2_2_bv100G/';
extension='.out';
%bdir='/shared/sp2rc2/Shared/simulations/smaug_realpmode/fastdata/cs1mkg/smaug/';
%rdirectory='spic_5b2_2_bv100G';

bdir='/Users/mikegriffiths/proj';
rdirectory='/washmc-data/uni11';

%directory=[bdir,rdirectory,'/matlabdat/'];
directory=[bdir,rdirectory,'/'];


B0=0.15;

gamma=1.666667;

mu=4.0*pi*1.0e-7;

%matfile=[directory,'vvzverustime.mat'];
matfile=[directory,'hhzverustime1.mat'];
load(matfile);
nt=533;
evelv=evelv2Mm_v;
evelb=evelv2Mm_bz;

t1=500;
t2=570;

evelv=evelv1Mm_v;
evelb=evelv1Mm_bz;

% cs=sqrt(gamma p/rho)
%
% 

%rho 1
% m1 2
% m2 3
% m3 4
% e 5
% bx 6
% by 7
% bz 8
% eb 9
% rhob 10
% b1b 11
% b2b 12
% b3b 13


 val1=reshape(wd(2,nrange,nrange,nrange),124,124,124);%z component vel
 val2=reshape(wd(1,nrange,nrange,nrange)+wd(10,nrange,nrange,nrange),124,124,124); %density
 val3=reshape(wd(1,nrange,nrange,nrange)+wd(10,nrange,nrange,nrange),124,124,124); %bz
 val4=reshape(wd(1,nrange,nrange,nrange)+wd(10,nrange,nrange,nrange),124,124,124); %energy


    val1=(val1./val2);




mod=reshape(evelv(:,:,t1),[124,124]);
mod1=reshape(evelv(:,:,t2),[124,124]);
mod2=reshape(evelb(:,:,t1),[124,124]);
mod3=reshape(evelb(:,:,t2),[124,124]);

figure(1);
subplot(2,2,1); surf(real(mod));  shading interp;   title('v '+string(t1));
view(0,90);
colorbar();
subplot(2,2,2); surf(real(mod1));  shading interp;   title('v '+string(t2));
view(0,90);
colorbar();
subplot(2,2,3); surf(real(mod2));  shading interp;   title('b '+string(t1));
view(0,90);
colorbar();
subplot(2,2,4); surf(real(mod3));  shading interp;   title('b '+string(t2));
view(0,90);
colorbar();




evelv=evelcor_vh;
evelb=evelcor_bz;

mod=reshape(evelv(:,:,t1),[124,124]);
mod1=reshape(evelv(:,:,t2),[124,124]);
mod2=reshape(evelb(:,:,t1),[124,124]);
mod3=reshape(evelb(:,:,t2),[124,124]);

figure(2);
subplot(2,2,1); surf(real(mod));  shading interp;   title('v '+string(t1));
view(0,90);
colorbar();
subplot(2,2,2); surf(real(mod1));  shading interp;   title('v '+string(t2));
view(0,90);
colorbar();
subplot(2,2,3); surf(real(mod2));  shading interp;   title('b '+string(t1));
view(0,90);
colorbar();
subplot(2,2,4); surf(real(mod3));  shading interp;   title('b '+string(t2));
view(0,90);
colorbar();

figure(3);

evelv=evelv1Mm_v;
evelb=evelv1Mm_bz;

ssvz=reshape(evelv(78,:,t1),[124,1]);
subplot(1,2,1);
plot(ssvz)
ylim([-2.5 2.5])

%hold on

%subplot(1,3,2)
subplot(1,2,2);
ssbz=reshape(10^5*evelb(78,:,t1),[124,1]);
plot(ssbz)
ylim([-20 20])








