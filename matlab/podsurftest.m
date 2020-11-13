

evelv=evelv2Mm_v;
evelb=evelv2Mm_bz;
subplot(2,2,1)
ss1=reshape(evelv(:,62,:),[124,1270]);
s1=surf(ss1);
s1.EdgeColor = 'none';
title('Vz');
subplot(2,2,2)
ss2=reshape(evelb(:,62,:),[124,1270]);
s2=surf(ss2);
title('Bz');
s2.EdgeColor = 'none';
subplot(2,2,3)
ss3=reshape(evelv(62,:,:),[124,1270]);
title('Vz');
s3=surf(ss3);
s3.EdgeColor = 'none';
subplot(2,2,4)
ss4=reshape(evelb(62,:,:),[124,1270]);
title('Bz');
s4=surf(ss4);
s4.EdgeColor = 'none';