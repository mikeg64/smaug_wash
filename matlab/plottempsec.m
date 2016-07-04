%%%load('/fastdata/cs1mkg/smaug/matlab_tempprofs/spic5b0_3d_vert_tempprofs.mat');
%%%load('/fastdata/cs1mkg/smaug/matlab_tempprofs/spic6b0_3d_rep_vandh_tempprofs.mat');

it=790;

figure;
subplot(2,2,1);
surf(reshape(etemptran1_h(it,:,:),124,124),'LineStyle','none');
hc=colorbar();
%title(gca,'Temperature for the 0,0 180.0s Driver (Horizontal Section in  Transition Layer at 2.0Mm )');
title(gca,'Horizontal Section in  Transition Layer at 2.0Mm ');
set(gca,'YTickLabel',{'0';'1.6';'3.2';'4.8'})
set(gca,'XTickLabel',{'0';'1.6';'3.2';'4.8'})

subplot(2,2,2);
surf(reshape(etemptran2_h(it,:,:),124,124),'LineStyle','none');
hc=colorbar();
%title(gca,'Temperature for the 0,0 Mode 180.0s Driver (Horizontal Section in Transition Layer at 2.3Mm)');
title(gca,'Horizontal Section in Transition Layer at 2.3Mm');
set(gca,'YTickLabel',{'0';'1.6';'3.2';'4.8'})
set(gca,'XTickLabel',{'0';'1.6';'3.2';'4.8'})

subplot(2,2,3);
surf(reshape(etempchrom_h(it,:,:),124,124),'LineStyle','none');
hc=colorbar();
%title(gca,'Temperature for the 0,0 Mode 180.0s Driver (Horizontal Section in Chromosphere at 0.94Mm)');
title(gca,'Horizontal Section in Chromosphere at 0.94Mm');
set(gca,'YTickLabel',{'0';'1.6';'3.2';'4.8'})
set(gca,'XTickLabel',{'0';'1.6';'3.2';'4.8'})

subplot(2,2,4);
surf(reshape(etempcor_h(it,:,:),124,124),'LineStyle','none');
%title(gca,'Temperature for the 0,0 Mode 180.0s Driver (Horizontal Section in Corona at 4.2Mm)');
title(gca,'Horizontal Section in Corona at 4.2Mm');
set(gca,'YTickLabel',{'0';'1.6';'3.2';'4.8'})
set(gca,'XTickLabel',{'0';'1.6';'3.2';'4.8'})

hc=colorbar();


figure;
subplot(2,2,1);
surf(reshape(etemp_v_x1(it,:,:),124,124),'LineStyle','none');
hc=colorbar();
%title(gca,'Temperature for the 0,0 Mode ( x dir)180.0s Driver (Vertical Section at y=2Mm )');
title(gca,'Vertical Section at y=2Mm ');
set(gca,'YTickLabel',{'0';'1.6';'3.2';'4.8'})
set(gca,'XTickLabel',{'0';'2.3';'4.6';'6.9'})


subplot(2,2,2);
surf(reshape(etemp_v_x2(it,:,:),124,124),'LineStyle','none');
hc=colorbar();
%title(gca,'Temperature for the 0,0 Mode ( x dir)180.0s Driver (Vertical Section at y=1.0Mm)');
title(gca,'Vertical Section at y=1.0Mm');
set(gca,'YTickLabel',{'0';'1.6';'3.2';'4.8'})
set(gca,'XTickLabel',{'0';'2.3';'4.6';'6.9'})




subplot(2,2,3);
surf(reshape(etemp_v_y1(it,:,:),124,124),'LineStyle','none');
hc=colorbar();
%title(gca,'Temperature for the 0,0 Mode ( y dir)180.0s Driver (Vertical Section at x=2Mm )');
title(gca,'Vertical Section at x=2Mm ');
set(gca,'YTickLabel',{'0';'1.6';'3.2';'4.8'})
set(gca,'XTickLabel',{'0';'2.3';'4.6';'6.9'})

subplot(2,2,4);
surf(reshape(etemp_v_y2(it,:,:),124,124),'LineStyle','none');
%title(gca,'Temperature for the 0,0 Mode ( y dir)180.0s Driver (Vertical Section at x=1.0Mm )');
title(gca,'Vertical Section at x=1.0Mm ');
set(gca,'YTickLabel',{'0';'1.6';'3.2';'4.8'})
set(gca,'XTickLabel',{'0';'2.3';'4.6';'6.9'})


hc=colorbar();
