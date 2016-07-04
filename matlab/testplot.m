



imfile=[ndirectory,'energyvtime_',id,nextension];


%surf(edifarray(1:900,38:124)','LineStyle','none');
surf(efluxarray(1:1175,38:124)','LineStyle','none');
hold on
hc=colorbar();
%caxis([0.5*10^4 -0.5*10^4]);
%set(hc,'Zlim',[0.5*10^4 -0.5*10^4]);
%caxis([0 0.003]);
%set(hc,'Zlim',[0 0.003]);

caxis([0 0.5e3]);
set(hc,'Zlim',[0 0.5e3]);

set(gca,'CameraPosition',[400 45 17320.508]);
%set(gca,'YTickLabel',{'0.09';'0.99';'1.94';'2.88';'3.83';'4.77';'5.72';'6.67'})
set(gca,'YTickLabel',{'1.78';'2.22';'2.68';'3.12';'3.57';'4.02';'4.47';'4.91';'5.36';'5.81'})


%colorbar;
xlabel(gca,'Time (seconds)');
ylabel(gca,'Height (Mm)');
title(gca,'Energy Dependence for the 0,1 Mode with a 307.7s Driver'); 
print('-djpeg', imfile); 


hold off
