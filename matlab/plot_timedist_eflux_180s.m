
%distance time plots created using 
%pvvt180_01.m
%pvvt300_01.m
%pvvt180_00.m
%pvvt300_00.m
%these generated from 


%ndirectory='/fastdata/cs1mkg/smaug/spic6b0_3d_rep/images';
%ndirectory='/fastdata/cs1mkg/smaug/spic5b0_3d/images';


%imfile=[ndirectory,'dt_',id,nextension];

%title(gca,'Distance Time Plot for the 0,0 Mode (y dir) 180.0s Driver (Horizontal Section in Chromosphere at 1Mm )'); 
%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Transition Layer at 2.06Mm )'); 
%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Corona at 4.3Mm )');
ptitle1='Distance Time Plot for the ';
ptitle2=' Mode 180.0s (Vertical Section at 2Mm x-dir)';




%yticks={'0.09';'0.99';'1.94';'2.88';'3.83';'4.77';'5.72';'6.67'};
yticks={'1.97';'2.44';'2.91';'3.38';'3.85';'4.31';'4.78';'5.25';'5.72';''};
%xticks={'0';'0.6667';'1.333';'2.0';'2.667';'3.333';'4.0'};






%0,0 mode
figure;
% <<<<<<< HEAD
% load('../../data/4b0_1_3dmatlab_perturb.mat');
% =======
load('washing_machvverustime.mat');
% >>>>>>> 7b9b1741b4d36d36fece34756a0c6e6a637c8f89

%load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_rep_xdir_vverustime.mat');
%load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_xdir_vverustime.mat');

%dtplot=evelchrom_vh;  %  horizontal section in chrom at  20
%dtplot=eveltran_vh;   %  horizontal section in transition layer at 42
%dtplot=evelcor_vh;    %  horizontal section in corona at 90

 dtplot=evel2Mm_vhy;  %vertical section at 2Mm  62
%dtplot=evel1Mm_vhx;  %vertical section at 1Mm  31
%dtplot=evelp5Mm_vhy;  %vertical section at 0.5Mm 15

%dtp00=dtplot(:,42:124)';
dtp00=dtplot';
smode='0,0';
%subplot(2,2,1);
%surf(real(dtp00'),'LineStyle','none');
surf(real(dtp00),'LineStyle','none');

zlimv=1e1*[-0.2 1];

 hold on
 hc=colorbar();
% caxis(zlimv);
% set(hc,'Zlim',zlimv);
% 
% set(gca,'CameraPosition',[400 45 17320.508]);
% 
% set(gca,'YTickLabel',yticks);
% %set(gca,'XTickLabel',xticks);
% 
% %colorbar;
% xlabel(gca,'Time (seconds)');
% %xlabel(gca,'Height (Mm)');
% ylabel(gca,'Distance (Mm)');


% ptitle=[smode,ptitle2];
% title(gca,ptitle);

%hold off


