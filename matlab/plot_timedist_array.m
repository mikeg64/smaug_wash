
%distance time plots created using 
%pvvt180_01.m
%pvvt300_01.m
%pvvt180_00.m
%pvvt300_00.m
%these generated from 


%ndirectory='/fastdata/cs1mkg/smaug/spic6b0_3d_rep/images';
%ndirectory='/fastdata/cs1mkg/smaug/spic5b0_3d/images';


%imfile=[ndirectory,'dt_',id,nextension];

%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Chromosphere at 1Mm )'); 
%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Transition Layer at 2.06Mm )'); 
%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Corona at 4.3Mm )');
ptitle1='Distance Time Plot for the ';
%ptitle2=' Mode 30.0s (Vertical Section at 2Mm x-dir)';
ptitle2=' Mode 30.0s';



%yticks={'0.09';'0.99';'1.94';'2.88';'3.83';'4.77';'5.72';'6.67'};
%old not used? yticks={'1.78';'2.22';'2.68';'3.12';'3.57';'4.02';'4.47';'4.91';'5.36';'5.81'};
%yticks={'0';'0.6667';'1.333';'2.0';'2.667';'3.333';'4.0'};

xticks={'0';'1.333';'3.666'};





%0,0 mode
figure;
load('/fastdata/cs1mkg/smaug/matlabdat/spicule4b0_3dtranint.mat');
%load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_xdir_vverustime.mat');

%dtplot=evelchrom_vh;  %  horizontal section in chrom at  20
dtplot=eveltran_vh;   %  horizontal section in transition layer at 42
%dtplot=evelcor_vh;    %  horizontal section in corona at 90

%dtplot=evel2Mm_vh;  %vertical section at 2Mm  62
%dtplot=evel1Mm_vh;  %vertical section at 1Mm  31
%dtplot=evelp5Mm_vh;  %vertical section at 0.5Mm 15
siz=size(dtplot);
dtp00=reshape(dtplot(62,:,:),124,siz(3));
smode='0,0';
subplot(1,3,1);
surf(real(dtp00'),'LineStyle','none');
zlimv=7e1*[-1 1];

hold on
hc=colorbar();
caxis(zlimv);
set(hc,'Zlim',zlimv);

view(0,90);
%set(gca,'CameraPosition',[400 45 17320.508]);

set(gca,'XTickLabel',xticks)
set(gca,'Xlim',[0 124]);

%colorbar;
ylabel(gca,'Time (seconds)');
%xlabel(gca,'Height (Mm)');
xlabel(gca,'Distance (Mm)');
set(gca,'Ylim',[0 siz(3)]);

ptitle=[smode,ptitle2];
title(gca,ptitle);

%hold off



clear('evelchrom_vh', 'eveltran_vh', 'evelcor_vh','evel2Mm_vh', 'evel1Mm_vh', 'evelp5Mm_vh' );

%0,1 mode
%figure;
%load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_rep_vverustime.mat');
%load('/fastdata/cs1mkg/smaug/matlabdat/spic5b0_1_3d_ydir_vverustime_1Mm.mat');
load('/fastdata/cs1mkg/smaug/matlabdat/spic5b0_3d5b0_tranint.mat');
%dtplot=evelchrom_vh;  %  horizontal section in chrom at  20
dtplot=eveltran_vh;   %  horizontal section in transition layer at 42
%dtplot=evelcor_vh;    %  horizontal section in corona at 90
%ptitle2=' Mode 180.0s (Vertical Section at 2Mm x-dir)';
ptitle2=' Mode 300.0s ';

%dtplot=evel2Mm_vh;  %vertical section at 2Mm  62
%dtplot=evel1Mm_vh;  %vertical section at 1Mm  31
%dtplot=evelp5Mm_vh;  %vertical section at 0.5Mm 15

siz=size(dtplot);
dtp01=reshape(dtplot(62,:,:),124,siz(3));
smode='0,0';
subplot(1,3,2);
surf(real(dtp01'),'LineStyle','none');
zlimv=10e2*[-2 1];

hold on
hc=colorbar();
caxis(zlimv);
set(hc,'Zlim',zlimv);

view(0,90);
%set(gca,'CameraPosition',[400 45 17320.508]);

set(gca,'XTickLabel',xticks)
set(gca,'Xlim',[0 124]);

%colorbar;
ylabel(gca,'Time (seconds)');
set(gca,'Ylim',[0 siz(3)]);
%xlabel(gca,'Height (Mm)');
xlabel(gca,'Distance (Mm)');


ptitle=[smode,ptitle2];
title(gca,ptitle);

%hold off


clear('evelchrom_vh', 'eveltran_vh', 'evelcor_vh','evel2Mm_vh', 'evel1Mm_vh', 'evelp5Mm_vh' );


%0,2 mode
%figure;
%load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_rep_vverustime.mat');
load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3dtranint.mat');
%ptitle2=' Mode 180.0s (Vertical Section at 2Mm x-dir)';
ptitle2=' Mode 180.0s ';

%dtplot=evelchrom_vh;  %  horizontal section in chrom at  20
dtplot=eveltran_vh;   %  horizontal section in transition layer at 42
%dtplot=evelcor_vh;    %  horizontal section in corona at 90

%dtplot=evel2Mm_vh;  %vertical section at 2Mm  62
%dtplot=evel1Mm_vh;  %vertical section at 1Mm  31
%dtplot=evelp5Mm_vh;  %vertical section at 0.5Mm 15

siz=size(dtplot);
dtp02=reshape(dtplot(62,:,:),124,siz(3));
smode='0,0';
subplot(1,3,3);
surf(real(dtp02'),'LineStyle','none');
zlimv=3.5e3*[-1 1];

%hold on
hc=colorbar();
caxis(zlimv);
set(hc,'Zlim',zlimv);

view(0,90);
%set(gca,'CameraPosition',[400 45 17320.508]);

set(gca,'XTickLabel',xticks)
set(gca,'Xlim',[0 124]);

%colorbar;
ylabel(gca,'Time (seconds)');
set(gca,'Ylim',[0 siz(3)]);
%xlabel(gca,'Height (Mm)');
xlabel(gca,'Distance (Mm)');


ptitle=[smode,ptitle2];
title(gca,ptitle);

%hold off




%following not needed when comparing 30,180 and 300

% 
% clear('evelchrom_vh', 'eveltran_vh', 'evelcor_vh','evel2Mm_vh', 'evel1Mm_vh', 'evelp5Mm_vh' );
% 
% % 
% %0,3 mode
% %figure;
% %load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_rep_vverustime.mat');
% %load('/fastdata/cs1mkg/smaug/matlabdat/spic5b0_3_3d_ydir_vverustime_0p5Mm.mat');
% load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3_3d_xdir_vverustime.mat');
% ptitle2=' Mode 180.0s (Vertical Section at 2Mm x-dir)';
% %dtplot=evelchrom_vh;  %  horizontal section in chrom at  20
% %dtplot=eveltran_vh;   %  horizontal section in transition layer at 42
% %dtplot=evelcor_vh;    %  horizontal section in corona at 90
% 
% dtplot=evel2Mm_vh;  %vertical section at 2Mm  62
% %dtplot=evel1Mm_vh;  %vertical section at 1Mm  31
% %dtplot=evelp5Mm_vh;  %vertical section at 0.5Mm 15
% 
% dtp03=dtplot;
% smode='0,3';
% subplot(2,2,4);
% surf(real(dtp03'),'LineStyle','none');
% zlimv=10e1*[-1 1];
% 
% %hold on
% hc=colorbar();
% caxis(zlimv);
% set(hc,'Zlim',zlimv);
% 
% set(gca,'CameraPosition',[400 45 17320.508]);
% 
% set(gca,'YTickLabel',yticks)
% 
% 
% %colorbar;
% xlabel(gca,'Time (seconds)');
% %xlabel(gca,'Height (Mm)');
% ylabel(gca,'Distance (Mm)');
% 
% 
% ptitle=[smode,ptitle2];
% title(gca,ptitle);
% 
% hold off
% 
% % 
% % 
% % 
% % 
% % 
% % 
% % 
% % 
