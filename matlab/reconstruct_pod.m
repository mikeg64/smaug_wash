
%reconstruct pod sample compute fourier transform to determin spectra

%first run the script tpod
% Reconstruction on mode k
k = 6; % for example

md=45;
Utilde_k_s = A_s(:,k)*PHI_s(:,k)';
% Normalization to match direct and snapshot modes (optional)
PHI = normc(PHI_s); % Spatial modes
A = U*PHI; % Time coefficients
Utilde_k = A(:,k)*PHI(:,k)'; % Reconstruction on mode k

st=reshape(Utilde_k,[nt,124,124]);



samp=reshape(st(25,:,:),124,124);

s=surf(samp);

s.EdgeColor = 'none';

tsamp=reshape(st(:,md,md),nt,1);


Fs=1;
L=nt;
Y = fft(tsamp);
%Compute the two-sided spectrum P2. Then compute the single-sided spectrum P1 based on P2 and the even-valued signal length L.

P2 = abs(Y/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
%Define the frequency domain f and plot the single-sided amplitude spectrum P1. The amplitudes are not exactly at 0.7 and 1, as expected, because of the added noise. On average, longer signals produce better frequency approximations.

f = 1000*Fs*(0:(L/2))/L;
plot(log10(f),log10(P1)) 
title('Single-Sided Amplitude Spectrum of X(t)')
xlabel('f (mHz)')
ylabel('|P1(f)|')

fftsurf=zeros(636,124);
for i=1:124
    tsamp=reshape(st(:,36,i),nt,1);
    Y = fft(tsamp);
    P2 = abs(Y/L);
    P1 = P2(1:L/2+1);
    P1(2:end-1) = 2*P1(2:end-1);
    fftsurf(:,i)=P1;
 
end

%     s=surf(fftsurf);
%     s.EdgeColor = 'none';
