




dt=1.0;
s0=2*dt;
ds= 0.5;
wname='morl';
NbSC=120;
SIG={esumarray(:,31),1};
SCA={s0,ds,NbSC};
WAV={wname,8};
cwts2=cwtft(SIG,'scales',SCA,'wavelet',WAV,'plot');

MorletFourierFactor = 4*pi/(6+sqrt(2+6^2));
Scales = cwts2.scales.*MorletFourierFactor;
Freq = 1./Scales;
figure
imagesc(t,[],abs(cwts2.cfs));
indices = get(gca,'ytick');
%set(gca,'yticklabel',Freq(indices));
xlabel('Time'); ylabel('Hz');
title('Time-Frequency Analysis with CWT');