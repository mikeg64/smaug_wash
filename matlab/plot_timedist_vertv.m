
%distance time plots created using 
%pvvt180_01.m
%pvvt300_01.m
%pvvt180_00.m
%pvvt300_00.m
%these generated from 


%ndirectory='/fastdata/cs1mkg/smaug/spic6b0_3d_rep/images';
%ndirectory='/fastdata/cs1mkg/smaug/spic5b0_3d/images';


directory='/fastdata-sharc/cs1mkg/smaug_wash/washmc_2p5_2p5_12p5_mach180_uni3/';
extension='.out';
bdir='/fastdata-sharc/cs1mkg/smaug_wash/';
rdirectory='washmc_2p5_2p5_12p5_mach180_uni3';



directory=[bdir,rdirectory,'/matlabdat/'];




%imfile=[ndirectory,'dt_',id,nextension];

%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Chromosphere at 1Mm )'); 
%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Transition Layer at 2.06Mm )'); 
%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Corona at 4.3Mm )');
%ptitle1='Distance Time Plot for the ';
%ptitle2=' Mode 300.0s (y-Vertical Section at 2Mm)';

ptitle1='';
ptitle2='';


yticks={'0.09';'0.99';'1.94';'2.88';'3.83';'4.77';'5.72';'6.67'};
%old not used? yticks={'1.78';'2.22';'2.68';'3.12';'3.57';'4.02';'4.47';'4.91';'5.36';'5.81'};
%%yticks={'0';'0.6667';'1.333';'2.0';'2.667';'3.333';'4.0'};






%0,0 mode
figure;
hold on;
matfile=[directory,'vzverustime.mat'];
load(matfile);

%load('/data/cs1mkg/smaug_realpmode/matlab/timedistplot/spic_4b2_2_bv20G_xdir_vvt.mat');
%load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_xdir_vverustime.mat');

%dtplot=evelchrom_vh;  %  horizontal section in chrom at  20
%dtplot=eveltran_vh;   %  horizontal section in transition layer at 42
%dtplot=evelcor_vh;    %  horizontal section in corona at 90

%dtplot=evel2Mm_vh;  %vertical section at 2Mm  62
%dtplot=evel1Mm_vh;  %vertical section at 1Mm  31
dtplot=evelp5Mm_vh;  %vertical section at 0.5Mm 15

dtp00=dtplot;
smode=' 0G';
subplot(2,2,1);
surf(real(dtp00'),'LineStyle','none');
zlimv=10*[-1 1];


xlimv=[0 600]; %time limit
ylimv=[0 124];

hc=colorbar();
caxis(zlimv);
%set(hc,'Zlim',zlimv);
set(gca,'Xlim',xlimv,'Ylim',ylimv);

 view(0,90);
%set(gca,'CameraPosition',[400 45 17320.508]);


set(gca,'YTickLabel',yticks)


%colorbar;
xlabel(gca,'Time (seconds)');
ylabel(gca,'Height (Mm)');
%xlabel(gca,'Distance (Mm)');
yticks={'0';'0.6667';'1.333';'2.0';'2.667';'3.333';'4.0'};


ptitle=[smode,ptitle2];
title(gca,ptitle);


clear('evelchrom_vh', 'eveltran_vh', 'evelcor_vh','evel2Mm_vh', 'evel1Mm_vh', 'evelp5Mm_vh' );






bdir='/shared/sp2rc2/Shared/simulations/smaug_realpmode/fastdata/cs1mkg/smaug/';
rdirectory='spic_5b2_2_bv50G';
directory=[bdir,rdirectory,'/matlabdat/'];




%imfile=[ndirectory,'dt_',id,nextension];

%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Chromosphere at 1Mm )'); 
%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Transition Layer at 2.06Mm )'); 
%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Corona at 4.3Mm )');
%ptitle1='Distance Time Plot for the ';
%ptitle2=' Mode 300.0s (y-Vertical Section at 2Mm)';



yticks={'0.09';'0.99';'1.94';'2.88';'3.83';'4.77';'5.72';'6.67'};
%old not used? yticks={'1.78';'2.22';'2.68';'3.12';'3.57';'4.02';'4.47';'4.91';'5.36';'5.81'};
%%yticks={'0';'0.6667';'1.333';'2.0';'2.667';'3.333';'4.0'};






%0,0 mode
%figure;
matfile=[directory,'spic_5b2_2_bv50G_ydir_vvt.mat'];
load(matfile);

%load('/data/cs1mkg/smaug_realpmode/matlab/timedistplot/spic_4b2_2_bv20G_xdir_vvt.mat');
%load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_xdir_vverustime.mat');

%dtplot=evelchrom_vh;  %  horizontal section in chrom at  20
%dtplot=eveltran_vh;   %  horizontal section in transition layer at 42
%dtplot=evelcor_vh;    %  horizontal section in corona at 90

%dtplot=evel2Mm_vh;  %vertical section at 2Mm  62
%dtplot=evel1Mm_vh;  %vertical section at 1Mm  31
dtplot=evelp5Mm_vh;  %vertical section at 0.5Mm 15

dtp00=dtplot;
smode=' 25G ';
subplot(2,2,2);
surf(real(dtp00'),'LineStyle','none');
zlimv=8*[-1 1];


xlimv=[0 400]; %time limit
ylimv=[0 124];

%hold on
hc=colorbar();
caxis(zlimv);
%set(hc,'Zlim',zlimv);
set(gca,'Xlim',xlimv,'Ylim',ylimv);

 view(0,90);
%set(gca,'CameraPosition',[400 45 17320.508]);


set(gca,'YTickLabel',yticks)


%colorbar;
xlabel(gca,'Time (seconds)');
ylabel(gca,'Height (Mm)');
%xlabel(gca,'Distance (Mm)');
%yticks={'0';'0.6667';'1.333';'2.0';'2.667';'3.333';'4.0'};


ptitle=[smode,ptitle2];
title(gca,ptitle);


clear('evelchrom_vh', 'eveltran_vh', 'evelcor_vh','evel2Mm_vh', 'evel1Mm_vh', 'evelp5Mm_vh' );








bdir='/shared/sp2rc2/Shared/simulations/smaug_realpmode/fastdata/cs1mkg/smaug/';
rdirectory='spic_5b2_2_bv25G';
directory=[bdir,rdirectory,'/matlabdat/'];




%imfile=[ndirectory,'dt_',id,nextension];

%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Chromosphere at 1Mm )'); 
%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Transition Layer at 2.06Mm )'); 
%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Corona at 4.3Mm )');
%ptitle1='Distance Time Plot for the ';
%ptitle2=' Mode 300.0s (y-Vertical Section at 2Mm)';



%yticks={'0.09';'0.99';'1.94';'2.88';'3.83';'4.77';'5.72';'6.67'};
%old not used? yticks={'1.78';'2.22';'2.68';'3.12';'3.57';'4.02';'4.47';'4.91';'5.36';'5.81'};
%%yticks={'0';'0.6667';'1.333';'2.0';'2.667';'3.333';'4.0'};






%0,0 mode
%figure;
matfile=[directory,'spic_5b2_2_bv25G_ydir_vvt.mat'];
load(matfile);

%load('/data/cs1mkg/smaug_realpmode/matlab/timedistplot/spic_4b2_2_bv20G_xdir_vvt.mat');
%load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_xdir_vverustime.mat');

%dtplot=evelchrom_vh;  %  horizontal section in chrom at  20
%dtplot=eveltran_vh;   %  horizontal section in transition layer at 42
%dtplot=evelcor_vh;    %  horizontal section in corona at 90

%dtplot=evel2Mm_v;  %vertical section at 2Mm  62
%dtplot=evel1Mm_v;  %vertical section at 1Mm  31
S=evelp5Mm_v;  %vertical section at 0.5Mm 15


%proper orthogonal decomposition
% https://depositonce.tu-berlin.de/bitstream/11303/9456/5/podnotes_aiaa2019.pdf

% Create snapshot matrixNt = length(S(1,1,:));S = reshape(permute(S, [3 2 1]), Nt, [ ]); % Reshape data into a matrix S with Nt rowsU = S - repmat(mean(S,1), Nt, 1); % Subtract the temporal mean from each row

% Create covariance matrix%C = (U'*U)/(Nt-1);% Solve eigenvalue problem%[PHI LAM] = eig(C,'vector');% Sort eigenvalues and eigenvectors%[lambda,ilam] = sort(LAM,'descend');%PHI = PHI(:, ilam); % These are the spatial modes% Calculate time coefficients%A = U*PHI;% Reconstruction on mode k%k = 1; % for example%Utilde_k = A(:,k)*PHI(:,k)';




% Create correlation matrixC_s = (U*U')/(Nt-1);


% Solve eigenvalue problem[A_s LAM_s] = eig(C_s,'vector');% Sort eigenvalues and eigenvectors[lambda_s,ilam_s] = sort(LAM_s,'descend');A_s = A_s(:, ilam_s); % These are the temporal modes% Calculate spatial coefficientsPHI_s = U'*A_s;% Reconstruction on mode kk = 1; % for exampleUtilde_k_s = A_s(:,k)*PHI_s(:,k)';% Normalization to match direct and snapshot modes (optional)PHI = normc(PHI_s); % Spatial modesA = U*PHI; % Time coefficientsUtilde_k = A(:,k)*PHI(:,k)'; % Reconstruction on mode k



% Singular value decomposition[L,SIG,R] = svd(U/sqrt(Nt-1));PHI = R; % PHI are the spatial modesA = U*PHI; % A are the time coefficientslambda = diag(SIG).^2; % lambda are the eigenvalues
