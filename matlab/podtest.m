

evelv=evelv2Mm_v;
evelb=evelv2Mm_bz;
subplot(1,2,1)
ss1=reshape(evelv(62,:,:),[124,1270]);
plot(ss1(62,:))
subplot(1,2,2)
ss2=reshape(evelb(:,62,:),[124,1270]);
plot(ss2(62,:))
