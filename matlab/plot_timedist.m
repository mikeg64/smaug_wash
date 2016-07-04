
%distance time plots created using 
%pvvt180_01.m
%pvvt300_01.m
%pvvt180_00.m
%pvvt300_00.m
%these generated from 


%ndirectory='/fastdata/cs1mkg/smaug/spic6b0_3d_rep/images';
ndirectory='/fastdata/cs1mkg/smaug/spic5b0_3d/images';
%load('/fastdata/cs1mkg/smaug/matlabdat/spic6b0_3d_rep_vverustime.mat');
load('/fastdata/cs1mkg/smaug/matlabdat/spic5b0_3d_vverustime.mat');


imfile=[ndirectory,'dt_',id,nextension];

%dtplot=evelchrom_vh;  %  horizontal section in chrom at  20
dtplot=eveltran_vh;   %  horizontal section in transition layer at 42
%dtplot=evelcor_vh;    %  horizontal section in corona at 90

%dtplot=evel2Mm_vh;  %vertical section at 2Mm  62
%dtplot=evel1Mm_vh;  %vertical section at 1Mm  31
%dtplot=evelp5Mm_vh;  %vertical section at 0.5Mm 15

fftt=fft2(dtplot(500:800,8:116));
% figure;
% surf(imag(fftt)','LineStyle','none');
% 
% figure;
ps=real(fftt).*real(fftt)+imag(fftt).*imag(fftt);
surf(real(ps'),'LineStyle','none');

%surf(edifarray(1:900,38:124)','LineStyle','none');
%surf(efluxarray(1:570,38:124)','LineStyle','none');

hold on
hc=colorbar();
caxis(5e3*[0 1]);
set(hc,'Zlim',5e3*[0 1]);
%caxis([0 0.003]);
%set(hc,'Zlim',[0 0.003]);

%caxis([0 0.25e2]);
%set(hc,'Zlim',[0 0.25e2]);

set(gca,'CameraPosition',[400 45 17320.508]);

set(gca,'YTickLabel',{'0.09';'0.99';'1.94';'2.88';'3.83';'4.77';'5.72';'6.67'})
%%set(gca,'YTickLabel',{'1.78';'2.22';'2.68';'3.12';'3.57';'4.02';'4.47';'4.91';'5.36';'5.81'})
%set(gca,'YTickLabel',{'0';'0.6667';'1.333';'2.0';'2.667';'3.333';'4.0'})


%colorbar;
xlabel(gca,'Time (seconds)');
%xlabel(gca,'Height (Mm)');
ylabel(gca,'Distance (Mm)');

%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Chromosphere at 1Mm )'); 
%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Transition Layer at 2.06Mm )'); 
%title(gca,'Distance Time Plot for the 0,0 Mode (x dir) 300.0s Driver (Horizontal Section in Corona at 4.3Mm )');

title(gca,'Distance Time Plot for the 0,0 Mode ( x dir)300.0s Driver (Vertical Section at 0.5Mm )');

%print('-djpeg', imfile); 


hold off
