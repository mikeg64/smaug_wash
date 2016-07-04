ptitle1='Distance Time Plot for the ';
%ptitle2=' Mode 180.0s (Vertical Section at 2Mm x-dir)';
ptitle2=' Mode.';



%yticks={'0.09';'0.99';'1.94';'2.88';'3.83';'4.77';'5.72';'6.67'};
%yticks={'1.78';'2.22';'2.68';'3.12';'3.57';'4.02';'4.47';'4.91';'5.36';'5.81'};
%%yticks={'0';'0.6667';'1.333';'2.0';'2.667';'3.333';'4.0'};






%0,0 mode
%figure;
load('../../data/4b0matlab_perturb.mat');

%load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_rep_xdir_vverustime.mat');
%load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_xdir_vverustime.mat');

%dtplot=evelchrom_vh;  %  horizontal section in chrom at  20
%dtplot=eveltran_vh;   %  horizontal section in transition layer at 42
%dtplot=evelcor_vh;    %  horizontal section in corona at 90

 dtplot=efluxarray;  %vertical section at 2Mm  62
%dtplot=evel1Mm_vh;  %vertical section at 1Mm  31
%dtplot=evelp5Mm_vh;  %vertical section at 0.5Mm 15

dtp00=dtplot;
smode='0,0';
subplot(2,2,1);
surf(real(dtp00'),'LineStyle','none');
% zlimv=1e3*[-1 1];

hold on
hc=colorbar();
% caxis(zlimv);
% set(hc,'Zlim',zlimv);

% set(gca,'CameraPosition',[400 45 17320.508]);

%set(gca,'YTickLabel',yticks)


%colorbar;
xlabel(gca,'Time (seconds)');
%xlabel(gca,'Height (Mm)');
ylabel(gca,'Distance (Mm)');


ptitle=[smode,ptitle2];
title(gca,ptitle);
