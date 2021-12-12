
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

nt=1625;
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

[U1, S1, V1] = svd(U.');

X = U.';    % in C^(spatio, temporal)

X1 = X(:, 1:end-1);
X2 = X(:, 2:end);
r=2;

Ur = U1(:, 1:r);
Sr = S1(1:r, 1:r);
Vr = V1(:, 1:r);
Atilde = Ur'*X2*Vr*Sr^(-1);
[W, D] = eig(Atilde);
Phi = X2*Vr*Sr^(-1)*W;   % DMD modes

%% generate grid geometry
xi = linspace(-10, 10, 400);
t = linspace(0, 4*pi, 200);
dt = t(2) - t(1);

[xgrid, tgrid] = meshgrid(xi, t);

%% create two spatio-temporal patterns
f1 = sech(xgrid + 3) .* (1*exp(1i*2.3*tgrid));
f2 = (sech(xgrid).*tanh(xgrid)).*(2*exp(1i*2.8*tgrid));

f = f1 + f2;

[u, s, v] = svd(f.');

%% plot
figure(1);
subplot(2,2,1); surfl(xgrid, tgrid, real(f1));  shading interp; colormap gray;  title('f1(x, t)');
subplot(2,2,2); surfl(xgrid, tgrid, real(f2));  shading interp; colormap gray;  title('f2(x, t)');
subplot(2,2,3); surfl(xgrid, tgrid, real(f));  shading interp; colormap gray; title('f(x, t) = f1(x, t) + f2(x, t)');

figure(2);
plot(diag(s) / sum(diag(s)), 'ro'); title('SVD: low rank property (rank = 2, two modes)');

figure(3);
subplot(2,1,1); plot(real(u(:, 1:3))); 
legend('1st mode of basis u (left singular vectors)', ...
        '2nd mode of basis u (left singular vectors)', ...
        '3rd mode; numerical round off (junk basis)  '); 
title('Modes for basis of column space of '' f ''');

subplot(2,1,2); plot(real(v(:, 1:3)));
legend('1st mode of basis v (right singular vectors)', ...
        '2nd mode of basis v (right singular vectors)', ...
        '3rd mode; numerical round off (junk basis)  '); 
title('Modes for basis of row space of '' f ''');

%% dynamic mode decomposition (DMD)
X = f.';    % in C^(spatio, temporal)

X1 = X(:, 1:end-1);
X2 = X(:, 2:end);

%% STEP 1: singular value decomposition (SVD)
r = 2;      % rank-r truncation
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

figure(4); 
subplot(2,1,1); plot(real(u(:, 1:2)));
legend('1st mode of SVD', ...
        '2nd mode of SVD'); 
subplot(2,1,2); plot(real(Phi));
legend('1st mode of DMD', ...
        '2nd mode of DMD'); 

%% STEP 5: reconstruct the signal
x1 = X(:, 1);       % time = 0
b = pinv(Phi)*x1;   % initial value; \: pseudo inverse

t_dyn = zeros(r, length(t));

for i = 1:length(t)
   t_dyn(:, i) = (b.*exp(omega*t(i))); 
end

f_dmd = Phi*t_dyn;

figure(1);
subplot(2,2,1); surfl(xgrid, tgrid, real(f1));  shading interp; colormap gray;  title('f1(x, t)');
subplot(2,2,2); surfl(xgrid, tgrid, real(f2));  shading interp; colormap gray;  title('f2(x, t)');
subplot(2,2,3); surfl(xgrid, tgrid, real(f));  shading interp; colormap gray; title('f(x, t) = f1(x, t) + f2(x, t)');
subplot(2,2,4); surfl(xgrid, tgrid, real(f_dmd).');  shading interp; colormap gray; title('reconstruction of f(x, t) by DMD');

%% additional informations
% predict furture state using time dynamics
t_ext = linspace(0, 8*pi, 400);

[xgrid_ext, tgrid_ext] = meshgrid(xi, t_ext);

t_ext_dyn = zeros(r, length(t_ext));

for i = 1:length(t_ext)
   t_ext_dyn(:, i) = (b.*exp(omega*t_ext(i))); 
end

f_dmd_ext = Phi*t_ext_dyn;

figure(4);
subplot(2,2,1); surfl(xgrid, tgrid, real(f));  shading interp; colormap gray; 
xlabel('spatial-axis'); ylabel('temporal-axis'); title('f(x, t) during t = [0, 4*pi]');
subplot(2,2,2); surfl(xgrid, tgrid, real(f_dmd).');  shading interp; colormap gray; 
xlabel('spatial-axis'); ylabel('temporal-axis'); title('DMD reconstruction of f(x, t) during t = [0, 4*pi]');
subplot(2,2,[3,4]); surfl(xgrid_ext, tgrid_ext, real(f_dmd_ext).');  shading interp; colormap gray; 
xlabel('spatial-axis'); ylabel('temporal-axis'); title('DMD prediction of f(x, t) during t = [0, 8*pi]');

% If eigen value: lambda or omega has tiny real part > 0,
% the output of system function which is spaned 
% by eigen vectors with eigen values goes to the infinity.
% It is one of the limitation of DMD method.

format long e;
disp(omega);    % eigen values exist on the imaginary part.
disp('real part: numerical round off');
disp('imag part: eigen values');