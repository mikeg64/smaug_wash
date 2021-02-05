%dynamic mode decomposition
%temporal decomposition
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
rdirectory='/washmc-data/uni1';

%directory=[bdir,rdirectory,'/matlabdat/'];
directory=[bdir,rdirectory,'/'];




%matfile=[directory,'vvzverustime.mat'];
matfile=[directory,'hhzverustime.mat'];
load(matfile);

%load('/data/cs1mkg/smaug_realpmode/matlab/timedistplot/spic_4b2_2_bv20G_xdir_vvt.mat');
%load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_xdir_vverustime.mat');

%dtplot=evelchrom_vh;  %  horizontal section in chrom at  20
%dtplot=eveltran_vh;   %  horizontal section in transition layer at 42
%dtplot=evelcor_vh;    %  horizontal section in corona at 90

%dtplot=evel2Mm_vh;  %vertical section at 2Mm  62
%dtplot=evel1Mm_vh;  %vertical section at 1Mm  31
%dtplot=evelp5Mm;  %vertical section at 0.5Mm 15

nt=1270;
%nt=635;
%S=evelv1Mm;  %vertical section at 0.5Mm 15
evelv=evelchrom_vh;
S=evelv(:,:,1:nt);
%proper orthogonal decomposition
% https://depositonce.tu-berlin.de/bitstream/11303/9456/5/podnotes_aiaa2019.pdf

% Create snapshot matrix
Nt = length(S(1,1,:));
S = reshape(permute(S, [3 2 1]), Nt, [ ]); % Reshape data into a matrix S with Nt rows
U = S - repmat(mean(S,1), Nt, 1); % Subtract the temporal mean from each row


% Create covariance matrix
%C = (U'*U)/(Nt-1);
% Solve eigenvalue problem
%[PHI LAM] = eig(C,'vector');
% Sort eigenvalues and eigenvectors
%[lambda,ilam] = sort(LAM,'descend');
%PHI = PHI(:, ilam); % These are the spatial modes
% Calculate time coefficients
%A = U*PHI;
% Reconstruction on mode k
%k = 1; % for example
%Utilde_k = A(:,k)*PHI(:,k)';




% Create correlation matrix
C_s = (U*U')/(Nt-1);


% Solve eigenvalue problem
[A_s LAM_s] = eig(C_s,'vector');
% Sort eigenvalues and eigenvectors
[lambda_s,ilam_s] = sort(LAM_s,'descend');
A_s = A_s(:, ilam_s); % These are the temporal modes
% Calculate spatial coefficients
PHI_s = U'*A_s;
% Reconstruction on mode k
k = 1; % for example
Utilde_k_s = A_s(:,k)*PHI_s(:,k)';
% Normalization to match direct and snapshot modes (optional)
PHI = normc(PHI_s); % Spatial modes
A = U*PHI; % Time coefficients
Utilde_k = A(:,k)*PHI(:,k)'; % Reconstruction on mode k



% Singular value decomposition
[L,SIG,R] = svd(U/sqrt(Nt-1));
PHI = R; % PHI are the spatial modes
A = U*PHI; % A are the time coefficients
lambda = diag(SIG).^2; % lambda are the eigenvalues
