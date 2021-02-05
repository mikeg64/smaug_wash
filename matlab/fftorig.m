nt=1270;
md=122;


bdir='/Users/mikegriffiths/proj';
rdirectory='/washmc-data/uni6';

%directory=[bdir,rdirectory,'/matlabdat/'];
directory=[bdir,rdirectory,'/'];




%matfile=[directory,'vvzverustime.mat'];
matfile=[directory,'hhzverustime.mat'];
load(matfile);






%nt=635;
%S=evelv1Mm;  %vertical section at 0.5Mm 15
evelv=evelv2Mm_v;
S=evelv(:,:,1:nt);

%proper orthogonal decomposition
% https://depositonce.tu-berlin.de/bitstream/11303/9456/5/podnotes_aiaa2019.pdf

% Create snapshot matrix
Nt = length(S(1,1,:));
%S = reshape(permute(S, [3 2 1]), Nt, [ ]); % Reshape data into a matrix S with Nt rows



tsamp=reshape(S(md,md,:),nt,1);


Fs=1;
L=nt;
Y = fft(tsamp);
%Compute the two-sided spectrum P2. Then compute the single-sided spectrum P1 based on P2 and the even-valued signal length L.

P2 = abs(Y/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
%Define the frequency domain f and plot the single-sided amplitude spectrum P1. The amplitudes are not exactly at 0.7 and 1, as expected, because of the added noise. On average, longer signals produce better frequency approximations.

f = 1000*Fs*(0:(L/2))/L;
%plot(log10(f),log10(P1)) 
plot(log10(f),log10(P1)) 
title('Single-Sided Amplitude Spectrum of X(t)')
xlabel('f (mHz)')
ylabel('|P1(f)|')

fftsurf=zeros(636,124);

for i=1:124
    tsamp=reshape(S(i,i,:),nt,1);
    Y = fft(tsamp);
    P2 = abs(Y/L);
    P1 = P2(1:L/2+1);
    P1(2:end-1) = 2*P1(2:end-1);
    fftsurf(:,i)=log10(P1);
 
end


h=gca
s=surf((fftsurf));
s.EdgeColor = 'none';
%zlim([-17 -5])
set(h,'yscale','log');
%set(h,'zscale','log');
colormap(jet);
colorbar()
view(2)
xlabel('Mode Number')
ylabel('Frequency (mHz)')






