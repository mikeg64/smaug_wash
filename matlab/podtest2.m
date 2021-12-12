
%routine to locate peaks

directory='/shared/sp2rc2/Shared/simulations/smaug_realpmode/fastdata/cs1mkg/smaug/spic_5b2_2_bv100G/';
extension='.out';
%bdir='/shared/sp2rc2/Shared/simulations/smaug_realpmode/fastdata/cs1mkg/smaug/';
%rdirectory='spic_5b2_2_bv100G';

bdir='/Users/mikegriffiths/proj';
rdirectory='/washmc-data/uni11';

%directory=[bdir,rdirectory,'/matlabdat/'];
directory=[bdir,rdirectory,'/'];




%matfile=[directory,'vvzverustime.mat'];
matfile=[directory,'hhzverustime1.mat'];
load(matfile);
nt=533;
evelv=evelv2Mm_v;
evelb=evelv2Mm_bz;
figure(1) 
%subplot(1,3,1)
ss1=reshape(evelv(62,:,1:nt),[124,nt]);
ss1f=ss1(62,:);
plot(log(abs(ss1(62,:))))
hold on

%subplot(1,3,2)

ss2=reshape(10^5*evelb(:,62,1:nt),[124,nt]);
ss2f=ss2(62,:);
plot(log(abs(ss2(62,:))))

hold on
%subplot(1,3,3)

%find peaks separated at least 30s
[pksvz,locsvz]=findpeaks(ss1(62,:),'MinPeakDistance',30);
[pksbz,locsbz]=findpeaks(ss2(62,:),'MinPeakDistance',30);

plot(locsvz,pksvz,'d')
plot(locsbz,pksbz,'o')

xlim([0 600])
ylim([-20 20])
%least squares fit
t=(48:1:nt)';
tbl = table(log(abs(ss1f(48:nt)')),t);
mdl = fitlm(tbl,'linear');

coeff=mdl.Coefficients.Estimate;
b=coeff(2); %slope
a=coeff(1); %intercept

shift1f=ss1f(48:1:nt)'-exp(-b.*t+a);

xtest=(48:1:nt);
ytest=b.*xtest+a;
figure(2)
plot(shift1f);
hold on
plot(xtest,ytest,'x');

t1=500;
t2=570;

evelv=evelv1Mm_v;
evelb=evelv1Mm_bz;


mod=reshape(evelv(:,:,t1),[124,124]);
mod1=reshape(evelv(:,:,t2),[124,124]);
mod2=reshape(evelb(:,:,t1),[124,124]);
mod3=reshape(evelb(:,:,t2),[124,124]);

figure(3);
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

figure(4);
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

figure(5);

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








