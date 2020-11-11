evelv=evelv2Mm_v;
evelb=evelv2Mm_bz;
figure 
ss1=reshape(evelv(62,:,1:650),[124,650]);
ss1f=ss1(62,:);
plot(ss1(62,:))
hold on
ss2=reshape(10^5*evelb(:,62,1:650),[124,650]);
ss2f=ss2(62,:);
plot(ss2(62,:))

hold on

%find peaks separated at least 30s
[pksvz,locsvz]=findpeaks(ss1(62,:),'MinPeakDistance',30);
[pksbz,locsbz]=findpeaks(ss2(62,:),'MinPeakDistance',30);

plot(locsvz,pksvz,'d')
plot(locsbz,pksbz,'o')
