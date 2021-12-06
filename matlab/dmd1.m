%distance time plots created using 
%pvvt180_01.m
%pvvt300_01.m
%pvvt180_00.m
%pvvt300_00.m
%these generated from 


%ndirectory='/fastdata/cs1mkg/smaug/spic6b0_3d_rep/images';
%ndirectory='/fastdata/cs1mkg/smaug/spic5b0_3d/images';


directory='/shared/sp2rc2/Shared/simulations/smaug_realpmode/fastdata/cs1mkg/smaug/spic_5b2_2_bv100G/';
extension='.out';
%bdir='/shared/sp2rc2/Shared/simulations/smaug_realpmode/fastdata/cs1mkg/smaug/';
%rdirectory='spic_5b2_2_bv100G';

bdir='/Users/mikegriffiths/proj';
rdirectory='/washmc-data/uni11';

%directory=[bdir,rdirectory,'/matlabdat/'];
directory=[bdir,rdirectory,'/'];


st=360;  %selected time

ks=[1 3 5 7 9 11]; %selected modes
%ks=[2 4 6 8 10 12]; %selected modes

%matfile=[directory,'vvzverustime.mat'];
matfile=[directory,'hhzverustime1.mat'];
load(matfile);

%load('/data/cs1mkg/smaug_realpmode/matlab/timedistplot/spic_4b2_2_bv20G_xdir_vvt.mat');
%load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_xdir_vverustime.mat');

%dtplot=evelchrom_vh;  %  horizontal section in chrom at  20
%dtplot=eveltran_vh;   %  horizontal section in transition layer at 42
%dtplot=evelcor_vh;    %  horizontal section in corona at 90

%dtplot=evel2Mm_vh;  %vertical section at 2Mm  62
%dtplot=evel1Mm_vh;  %vertical section at 1Mm  31
%dtplot=evelp5Mm;  %vertical section at 0.5Mm 15

nt=800;
dt=1;
t = linspace(0, nt, nt);
%nt=635;
%S=evelv1Mm;  %vertical section at 0.5Mm 15
evelv=evelchrom_vh;
S=evelv(:,:,1:nt);
%proper orthogonal decomposition
% https://depositonce.tu-berlin.de/bitstream/11303/9456/5/podnotes_aiaa2019.pdf

% Create snapshot matrix
Nt = length(S(1,1,:));
S = reshape(permute(S, [3 2 1]), Nt, [ ]); % Reshape data into a matrix S with Nt rows
SU = S - repmat(mean(S,1), Nt, 1); % Subtract the temporal mean from each row

[u, s, v] = svd(SU.');


%% dynamic mode decomposition (DMD)
X = SU.';    % in C^(spatio, temporal)

X1 = X(:, 1:end-1);
X2 = X(:, 2:end);


%% STEP 1: singular value decomposition (SVD)
r = 10;      % rank-r truncation
[U, S, V] = svd(X1, 'econ');

Ur = U(:, 1:r);
Sr = S(1:r, 1:r);
Vr = V(:, 1:r);


%% STEP 2: low-rank subspace matrix 
%         (similarity transform, least-square fit matrix, low-rank subspace matrix)
Atilde = Ur'*X2*Vr*Sr^(-1);


%% STEP 3: eigen decomposition
% W: eigen vectors
% D: eigen values
[W, D] = eig(Atilde);


%% STEP 4: real space DMD mode
Phi = X2*Vr*Sr^(-1)*W;   % DMD modes

lamdba = diag(D);       % eigen value
omega = log(lamdba)/dt; % log of eigen value

%% STEP 5: reconstruct the signal
x1 = X(:, 1);       % time = 0
b = pinv(Phi)*x1;   % initial value; \: pseudo inverse

t_dyn = zeros(r, length(t));

for i = 1:length(t)
   t_dyn(:, i) = (b.*exp(omega*t(i))); 
end

f_dmd = Phi*t_dyn;




%% additional informations
% predict furture state using time dynamics
t_ext = linspace(0, pi, 5);

%[xgrid_ext, tgrid_ext] = meshgrid(xi, t_ext);

t_ext_dyn = zeros(r, length(t_ext));

for i = 1:length(t_ext)
   t_ext_dyn(:, i) = (b.*exp(omega*t_ext(i))); 
end

f_dmd_ext = Phi*t_ext_dyn;

%% plot results
% 
mod=reshape(f_dmd(:,10),[124,124]);
mod1=reshape(SU(10,:)',[124,124]);
figure(1);
subplot(1,2,1); surf(real(mod));  shading interp;   title('f1(x, t)');
subplot(1,2,2); surf(real(mod1));  shading interp;   title('f2(x, t)');
%subplot(2,2,3); surf();  shading interp;  title('f(x, t) = f1(x, t) + f2(x, t)');



