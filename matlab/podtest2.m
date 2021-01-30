
%routine to locate peaks

directory='/shared/sp2rc2/Shared/simulations/smaug_realpmode/fastdata/cs1mkg/smaug/spic_5b2_2_bv100G/';
extension='.out';
%bdir='/shared/sp2rc2/Shared/simulations/smaug_realpmode/fastdata/cs1mkg/smaug/';
%rdirectory='spic_5b2_2_bv100G';

bdir='/Users/mikegriffiths/proj';
rdirectory='/washmc-data/uni6';

%directory=[bdir,rdirectory,'/matlabdat/'];
directory=[bdir,rdirectory,'/'];




%matfile=[directory,'vvzverustime.mat'];
matfile=[directory,'hhzverustime.mat'];
%load(matfile);
nt=900;
evelv=evelv2Mm_v;
evelb=evelv2Mm_bz;
figure 
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


%least squares fit
t=(48:1:nt)';
tbl = table(log(abs(ss1f(48:nt)')),t);
mdl = fitlm(tbl,'linear');

coeff=mdl.Coefficients.Estimate;
b=coeff(2); %slope
a=coeff(1); %intercept

shift1f=ss1f'-exp(-b.*t+a);

xtest=(48:1:nt);
ytest=b.*xtest+a;
figure
plot(shift1f);
hold on
plot(xtest,ytest,'x');
