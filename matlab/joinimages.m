



nimages=965;

directory='/fastdata/cs1mkg/smaug/washmc_2p5_2p5_12p5_180_kg/';

%dir1=[directory, 'images_densslices_19_25/'];
%dir2=[directory, 'images_densslices_49_55/'];
%dir3=[directory, 'images_densslices_89_95/'];
%dirf=[directory, 'images_densslices_imjoin/'];

dir1=[directory, 'images_pksecs_vquiv_6/'];
dir2=[directory, 'images_pksecs_vquiv_10/'];
dir3=[directory, 'images_pksecs_vquiv_30/'];
dirf=[directory, 'images_pksecs_vquiv_imjoin/'];



for i=1:10:nimages
    
  id=int2str(i*1000)
  fim1=[dir1,'im1_',id,'.jpg'];
  fim2=[dir2,'im1_',id,'.jpg'];
  fim3=[dir3,'im1_',id,'.jpg'];
  
  imjoinfile=[dirf,'im1_',id,'.jpg'];
  
  im1=imread(fim1);
  im2=imread(fim2);
  im3=imread(fim3);
  
  imf=[im1,im2,im3];
  image(imf);
  hold on;
  set(gca, 'Visible', 'off');
  set(gca, 'Box', 'off');
  %set(gcf,'Position', [1 1 2520 856]);
  set(gcf,'Position', [1 1 1650 440]);
  
  imwrite(imf,imjoinfile);
  %print('-djpeg', imjoinfile,'Position', [1 1 1650 440]);
  
  
  F(i)=getframe;
  
  
end

movie(F);
% hf=figure;
% set(hf,'Position',[1 1 1650 440]);
% axis off;

% movie(hf,F)

hold off;

