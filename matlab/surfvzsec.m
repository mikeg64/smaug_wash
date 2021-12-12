directory='/shared/sp2rc2/Shared/simulations/smaug_realpmode/fastdata/cs1mkg/smaug/spic_5b2_2_bv100G/';
extension='.out';
%bdir='/shared/sp2rc2/Shared/simulations/smaug_realpmode/fastdata/cs1mkg/smaug/';
%rdirectory='spic_5b2_2_bv100G';

bdir='/Users/mikegriffiths/proj';
rdirectory='/washmc-data/uni11';
nextension='.jpg';
%directory=[bdir,rdirectory,'/matlabdat/'];
directory=[bdir,rdirectory,'/'];
matfile=[directory,'washmc__400000.out'];
i=300;
B0=0.15;

gamma=1.666667;

mu=4.0*pi*1.0e-7;





id=int2str(1000*i);
filename=[directory,'washmc__',id,extension];
timetext=['time=',int2str(i),'s'];
imfile=[directory,'im1_',id,nextension];
disp([id filename]);
   fid=fopen(trim(filename));
   %fseek(fid,pictsize(ifile)*(npict(ifile)-1),'bof');
   headline=trim(setstr(fread(fid,79,'char')'));
   it=fread(fid,1,'integer*4'); time=fread(fid,1,'float64');
 
   ndim=fread(fid,1,'integer*4');
   neqpar=fread(fid,1,'integer*4'); 
   nw=fread(fid,1,'integer*4');
   nx=fread(fid,3,'integer*4');
   
   nxs=nx(1)*nx(2)*nx(3);
   varbuf=fread(fid,7,'float64');
   
   gamma=varbuf(1);
   eta=varbuf(2);
   g(1)=varbuf(3);
   g(2)=varbuf(4);
   g(3)=varbuf(5);
   
   
   varnames=trim(setstr(fread(fid,79,'char')'));
   
   for idim=1:ndim
      X(:,idim)=fread(fid,nxs,'float64');
   end
   
   for iw=1:nw
      %fread(fid,4);
      w(:,iw)=fread(fid,nxs,'float64');
      %fread(fid,4);
   end
   
   nx1=nx(1);
   nx2=nx(2);
   nx3=nx(3);
   
   xx=reshape(X(:,1),nx1,nx2,nx3);
   yy=reshape(X(:,2),nx1,nx2,nx3);
   zz=reshape(X(:,3),nx1,nx2,nx3);
   
   
 
  % extract variables from w into variables named after the strings in wnames
wd=zeros(nw,nx1,nx2,nx3);
for iw=1:nw
  
     tmp=reshape(w(:,iw),nx1,nx2,nx3);
     wd(iw,:,:,:)=tmp;
end


%w=tmp(iw);
  

clear tmp; 
   
   
   fclose(fid);




%plot sections through 3d array
   %slice=48;
   x=linspace(0,4,128);
   y=linspace(0,4,128);
   z=linspace(0,6,128);
   
   
   
   
   nrange=3:126;
   
   ax=x(nrange);
   ay=y(nrange);
   az=z(nrange);
   [x1,x2,x3] = meshgrid(ax,ay,az);
     val1=reshape(wd(2,nrange,nrange,nrange),124,124,124);%z component
%     val1=reshape(wd(3,nrange,nrange,nrange),124,124,124);
%    val3=reshape(wd(4,nrange,nrange,nrange),124,124,124);
     val2=reshape(wd(1,nrange,nrange,nrange)+wd(10,nrange,nrange,nrange),124,124,124);

%     val1=reshape(wd(6,nrange,nrange,nrange)+wd(11,nrange,nrange,nrange),124,124,124);
%      val2=reshape(wd(7,nrange,nrange,nrange)+wd(12,nrange,nrange,nrange),124,124,124);
%      val3=reshape(wd(8,nrange,nrange,nrange)+wd(13,nrange,nrange,nrange),124,124,124);
%   val1=reshape((wd(1,nrange,nrange,nrange)),124,124,124);
%     val1=reshape(wd(6,nrange,nrange,nrange),124,124,124);
%      val2=reshape(wd(7,nrange,nrange,nrange),124,124,124);
%      val3=reshape(wd(8,nrange,nrange,nrange),124,124,124);
%   val1=abs(val1)+(1e-11);

    val1=(val1./val2);
%    val3=(val3./val2);

%    val4=sqrt(val1.^2 + val3.^2+val2.^2);
%    val4=(val1.^2 );
   
%    myval=shiftdim(log10(val1),1);
    %myval=shiftdim(log10(val4),1);
%     myval=shiftdim(val4,1);
   myval=shiftdim(val1,1);
	R=8.3e+003;
	mu=1.257E-6;
	mu_gas=0.6;
	gamma=1.66667;

 % sabx=reshape(wd(11,nrange,nrange,nrange),124,124,124);
%saby=reshape(wd(12,nrange,nrange,nrange),124,124,124);
%sabz=reshape(wd(13,nrange,nrange,nrange),124,124,124);
%TP=reshape(wd(9,nrange,nrange,nrange),124,124,124);
%TP=TP-(sabx.^2.0+saby.^2.0+sabz.^2.0)./2.0;
%TP=(gamma-1.d0).*TP;



   %mval is T
  
   %mytval=shiftdim(mu_gas.*TP./R./val2,1);  
    
    


   %P = [2 1 3];
   %x1 = permute(x1, P);
   %x2 = permute(x2, P);
   %x3 = permute(x3, P);
   %myval = permute(myval, P);
   
   
  %h= slice(myval,64, 64, 4);
  %figure('Visible','off','IntegerHandle','Off');
  hold on;
  %h=slice(myval,80, 64,8);
  %h=slice(myval,96, 96,[5 49 100]);  %used for 0,1 mode
  %h=slice(myval,96, 96,[5 49 100]);  %used for 1,1 mode
 % h=slice(myval,108, 108,[5 49 85]);  %used for 2,2 mode
  %h=slice(myval,108, 108,[5 49]);  %used for 2,2 mode
  %h=slice(myval,108, 96,[5 49 100]);  %used for 0,1 mode
  %h=slice(myval,32, 32,[5 49 100]);  %used for 0,0 mode
  %h=slice(myval,65, 65,[5 49 100]);
  %h=slice(myval,105, 96,8);
  %sect=myval( :,:,2);
 sect=myval( :,:,3);
%   for isect=50:55
%     sect=sect+myval( :,:,isect);  
%   end
%  sect=myval( :,:,2);
 h=surf(sect','LineStyle','none');
   view(0,90);
 %view(-37.5,15);
%   set(gca,'CameraPosition',[70 70 17820]);
%   set(gca,'CameraTarget',[70 70 70]);
%   set(gca,'CameraViewAngle',6.6086103);
%   set(gca,'CameraUpVector',[0 1 0]);
set(gca,'Xlim',[0 124],'Ylim',[0 124]);



  hold on;
   set(h,'EdgeColor','none','FaceColor','interp');
  
  
  
%    % hcs=contourslice(mytval,[],[],[35 49 80]);
%   hcs=contourslice(mytval,[],[],[49 80]);
%   colors = get(hcs,'cdata');
% colors=unique(cat(1,colors{:}));
% colors=colors(~isnan(colors));
% 
% 
% % Loop through all the patches returned by CONTOURSLICE, 
% % and designate a linestyle for each
% % Define the line style (note that this can be changed 
% % since the code is written generally)
% linespec = {'-','--',':','-.'};
% %linecspec = {'-','--',':','-.'};
% linestyles = repmat(linespec,1,ceil(length(colors)/length(linespec)));
% linestyles = {linestyles{1:length(colors)}};
% 
% 
% for n=1:length(hcs)
%     % Find the unique color number associated with the handle
%     color = find(max(get(hcs(n),'cdata'))==colors);
%     % Convert the color to the associated linestyle
%     linestyle = linestyles{color};
%     set(hcs(n),'linestyle',linestyle);
% end

  
  
  
  
  
  
  
  
  %grid off;
  %set(h,'XData',ax,'YData',ay,'ZData',az);
  %hax=get(h,'Children');
  %set(gca,'CameraPosition',[-606.298 -914.02 280.537]);
  %set(gca,'Xlim',[0 124],'Ylim',[0 124],'Zlim',[0 124]);
  
 % set(gca,'XTickLabel',{'0';'.31';'.63';'.94';'1.25';'1.56';'1.88'})
 % set(gca,'YTickLabel',{'0';'.31';'.63';'.94';'1.25';'1.56';'1.88'})
  %set(gca,'YTickLabel',{'0';'1.6';'3.2'})



  %set(gca,'YTickLabel',{'0';'1.6';'3.2'})
  %set(gca,'XTickLabel',{'0';'0.63';'1.26';'1.89';'2.52';'3.15';'3.78'})
  %set(gca,'ZTickLabel',{'0.09';'0.99';'1.94';'2.88';'3.83';'4.77';'5.72'})
  %cmap=colormap('Jet');
  
  
  
       max1=max(sect);
      max2=max(max1);
      max3=max(max2);

      min1=min(sect);
      min2=min(min1);
      min3=min(min2);
      
%  if i==1
%         minval=min3;
%         maxval=max3;
%  else
%     if mod(i,100)==0
      minval=min3;
      maxval=max3;        
%     end   
% end 
% minval=0.0;
% maxval=5.0e-21;

      
%       min1=min(sect);
%       minval=min(min1);
      
%       max1=max(sect);
%       maxval=max(sect);
      
      % mval=1e-8;
      % maxval=mval;
      % minval=-mval;
      %minval=-3e-5;
      %maxval=3e-5;

%       if min3<minval
%           minval=min3;
%       end
% 
%       if max3>maxval
%           maxval=max3;
%       end
% 
%        if min3 < -mval
%              minval=-mval;
%        end
%  
%        if max3 >mval
%            maxval=mval;
%        end
       
%        maxval=max3;
%        minval=min3;
%  minval=0;
%  minval=-15;
%maxval=-10;
%  minval=-3e-5;
% maxval=3e-5;

  
    minval=-50;
     maxval=50;
  cmap=colormap(jet(256));
  caxis([minval maxval]);
  %caxis([-0.6 0.6]);
  %caxis([4*10^5 3*10^6]);
  divmap=diverging_map(linspace(0,1,256),[0.23 0.299 0.754],[0.706 0.016 0.15]);
  colormap(divmap);
  %colormap(cmap);
  
  
 
  
  
  hc=colorbar();
  
%    set(hc,'Ylim',[minval maxval]);
 
  %set(hc,'Ylim',[-0.6 0.6]);
  %set(hc,'Ylim',[4*10^5 3*10^6]);
   text(5,128,timetext);
%   %title('Vertical Velocity for Solar Atmosphere with a Sinusoidal (0,0) Mode Driver of Period673.4s, Applied at a Height of 100km');
%   title('Vertical Velocity for Solar Atmosphere with a Sinusoidal (3,3) Mode Driver of Period 100.0s, Applied at a Height of 100km');
%   xlabel('x-distance (Mm)');
%   ylabel('y-distance (Mm)');
%   zlabel('Height (Mm)');
%   
%   ylabel(hc,'Vz [m/s]');
  
  
  
  print('-djpeg', imfile);
  
  hold off
