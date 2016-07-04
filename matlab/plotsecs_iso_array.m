   


%for i=9:1:9
itstep=0;
 %for i=0:10:581   
  for i=200:1:200     
    directory='/fastdata/cs1mkg/smaug/spic2p82a_0_0_b20gv/';
extension='.out';

ndirectory='/fastdata/cs1mkg/smaug/spic2p82a_0_0_b20gv/imagesisostream/';
nextension='.jpg';
%for i=200:200
%for i=0:5:30    

id=int2str(1000*i);
filename=[directory,'zerospic1__',id,extension];
imfile=[ndirectory,'im1_',id,nextension];
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
   
   xmin=3;
   xmax=126;
   ymin=3;
   ymax=126;  
    
   
   nrange=3:126;
   
   ax=x(nrange);
   ay=y(nrange);
   az=z(nrange);

      xsec=1:4:128;
   ysec=1:4:128;
   nx=32;
   ny=32;
   
 
   
   
   
    % Decide where in data space you want to plot cones. This example selects the 
    % full range of x and y in eight steps and the range 3 to 15 in four steps in z 
    % using linspace and meshgrid.
    nxrange = linspace(xmin,xmax,8);
    nyrange = linspace(ymin,ymax,8);
    nzrange = 3:4:126;
    [cx cy cz] = meshgrid(nxrange,nyrange,nzrange);
    
    

    









   %plot sections through 3d array
   %slice=48;
   x=linspace(0,4,128);
   y=linspace(0,4,128);
   z=linspace(0,6,128);
   
   
   
   
   nrange=3:126;
   
   ax=x(nrange);
   ay=y(nrange);
   az=z(nrange);
   [x1,x2,x3] = meshgrid(nrange,nrange,nrange);
   

   val3=reshape(wd(6,nrange,nrange,nrange)+wd(11,nrange,nrange,nrange),124,124,124);
   uu=shiftdim(val3,1);
 val3=reshape(wd(7,nrange,nrange,nrange)+wd(12,nrange,nrange,nrange),124,124,124);
   uv=shiftdim(val3,1);
  val3=reshape(wd(8,nrange,nrange,nrange)+wd(13,nrange,nrange,nrange),124,124,124);
   uw=shiftdim(val3,1);
   
   umag=sqrt(uu.*uu+uv.*uv+uw.*uw);
   
   
      val1=reshape(wd(2,nrange,nrange,nrange),124,124,124);
   val2=reshape(wd(1,nrange,nrange,nrange)+wd(10,nrange,nrange,nrange),124,124,124);


   myval=shiftdim(val1./val2,1);
   
   %beta=gas pressure/magnetic pressure
   %beta=pk/(B_0^2/2mu)
   %compute pressure
   R=8.3e+003;
	mu=1.257E-6;
	mu_gas=0.6;
	gamma=1.66667;
    
    magb=reshape(sqrt(wd(11,nrange,nrange,nrange).^2+wd(12,nrange,nrange,nrange).^2+wd(13,nrange,nrange,nrange).^2),124,124,124);
    magp=reshape(sqrt(wd(6,nrange,nrange,nrange).^2+wd(7,nrange,nrange,nrange).^2+wd(8,nrange,nrange,nrange).^2),124,124,124);

% original beta computation by MKG June 2015
% TP=reshape(wd(5,nrange,nrange,nrange)+0.5.*(wd(2,nrange,nrange,nrange).^2+wd(3,nrange,nrange,nrange).^2+wd(4,nrange,nrange,nrange).^2)./(wd(1,nrange,nrange,nrange)+wd(9,nrange,nrange,nrange)),124,124,124);
% TP=TP-magb.*magp-0.5.*magp.*magp-0.5*magb.*magb+reshape(wd(10,nrange,nrange,nrange),124,124,124);
% 
% %TP=TP-(umag.*umag)./2.0;
% TP=(gamma-1.d0).*TP;
% mu=1;
% beta=mu.*TP./(0.5*(magb.*magb+magp.*magp)+magp.*magb);    
    
    
    
%  beta computation from IDL routine   
%   T=dblarr(n1,n2,n3)
% T[*,*,*]=(w[*,*,*,4]+w[*,*,*,8])
% T[*,*,*]=T[*,*,*]-(w[*,*,*,1]^2.0+w[*,*,*,2]^2.0+w[*,*,*,3]^2.0)/(w[*,*,*,0]+w[*,*,*,9])/2.0
% T[*,*,*]=T[*,*,*]-((w[*,*,*,5]+w[*,*,*,10])^2.0+(w[*,*,*,6]+w[*,*,*,11])^2.0+(w[*,*,*,7]+w[*,*,*,12])^2.0)/2.d0
% beta=dblarr(n1,n2,n3)
% beta[*,*,*]=(((w[*,*,*,5]+w[*,*,*,10])*sqrt(mu)*1.0e4)^2.0+((w[*,*,*,6]+w[*,*,*,11])*sqrt(mu)*1.0e4)^2.0+$
%               ((w[*,*,*,7]+w[*,*,*,12])*sqrt(mu)*1.0e4)^2.0)/2.0/((gamma-1.d0)*T[*,*,*])
%   
    
    
 
%beta computation updated using IDL
TP=reshape(wd(5,nrange,nrange,nrange)+wd(9,nrange,nrange,nrange),124,124,124);
TP=TP-0.5*reshape((wd(2,nrange,nrange,nrange).^2+wd(3,nrange,nrange,nrange).^2+wd(4,nrange,nrange,nrange).^2)./(wd(1,nrange,nrange,nrange)+wd(10,nrange,nrange,nrange)),124,124,124);
TP=TP-0.5*reshape((wd(6,nrange,nrange,nrange)+wd(11,nrange,nrange,nrange)).^2+(wd(7,nrange,nrange,nrange)+wd(12,nrange,nrange,nrange)).^2+(wd(8,nrange,nrange,nrange)+wd(13,nrange,nrange,nrange)).^2,124,124,124);

beta=0.5*mu*1.0d8*reshape((wd(6,nrange,nrange,nrange)+wd(11,nrange,nrange,nrange)).^2+(wd(7,nrange,nrange,nrange)+wd(12,nrange,nrange,nrange)).^2+(wd(8,nrange,nrange,nrange)+wd(13,nrange,nrange,nrange)).^2,124,124,124)./((gamma-1.0d0).*TP);

   
   
  
   
   
   
   

   
   % Draw the cones, setting the scale factor to 5 to make the cones larger than 
    % the default size:
    %hcones = coneplot(x1,x2,x3,uu,uv,uw,cx,cy,cz,5);
    % Set the coloring of each cone using FaceColor and EdgeColor:
    %set(hcones,'FaceColor','red','EdgeColor','none')
    
    [sx,sy,sz] = meshgrid(nxrange,nyrange,1);
    %plot3(sx(:),sy(:),sz(:),'*r');
    zmax = max(x3(:)); zmin = min(x3(:));

    %streamline(x1,x2,x3,uu,uv,uw,sx(:),sy(:),sz(:))
     
    
    %streamline(x1,x2,x3,uu,uv,uw)
%streamline(uu,uv,uw)
    % Calculate the magnitude of the vector field (which represents wind speed) to 
    % generate scalar data for the slice command:
   % hold on
   
   
   %P = [2 1 3];
   %x1 = permute(x1, P);
   %x2 = permute(x2, P);
   %x3 = permute(x3, P);
   %myval = permute(myval, P);
   
   
  %h= slice(myval,64, 64, 4);
  %h=figure();
  %hold on;
   maxv=max(max(max(beta)));
minv=min(min(min(beta)));
  %isovalue=0.1909;
  isovalue=minv+(maxv-minv)/2;
  
  itstep=itstep+1;
  maxva(itstep)=maxv;
  minva(itstep)=minv;
  ava(itstep)=minv+(maxv-minv)/2;
    % isovalue=0.1746;
     fv = patch(isosurface(x1,x2,x3,beta,isovalue));
      isonormals(x1,x2,x3,beta,fv)
     set(fv,'FaceColor','red','EdgeColor','none'); 
      daspect([1,1,1])
view(3); 
axis tight;
camlight; 
lighting gouraud ;
       
       hold on;
       
       streamslice(x1,x2,x3,uu,uv,uw,0.5*(zmax-zmin),[],[],0.5);  
       
     %h=slice(myval,65, 65,[5 49 100]); 
     h=slice(myval,[], [],[5 49 100]); 
       
       
       
       hold on;
       set(h,'EdgeColor','none','FaceColor','interp');
       
      %set(h,'XData',ax,'YData',ay,'ZData',az);
      hax=get(h,'Children');
      
      
     
      
      
     % set(gca,'CameraPosition',[911.383 -585.056 176.313]);
      set(gca,'CameraPosition',[491.298 -661.02 631.537]);
      set(gca,'Xlim',[0 124],'Ylim',[0 124],'Zlim',[0 124]);

      set(gca,'XTickLabel',{'0';'1.6';'3.2'})
      set(gca,'YTickLabel',{'0';'1.6';'3.2'})
      set(gca,'ZTickLabel',{'0.09';'0.99';'1.94';'2.88';'3.83';'4.77';'5.72'})
      cmap=colormap('Jet');
      %caxis([-4000 5000]);
      caxis([-0.0044 0.0027]);
      
         max1=max(myval);
  max2=max(max1);
  max3=max(max2);
  
  min1=min(myval);
  min2=min(min1);
  min3=min(min2);
  
  maxval=10;
  minval=-10;
  
  if min3<minval
      minval=min3;
  end
  
  if max3>maxval
      maxval=max3;
  end
  
  if minval > -200
        minval=-200;
  end
  
  if maxval<200
      maxval=200;
  end
  
  cmap=colormap(jet(256));
  caxis([minval maxval]);
  %caxis([-0.6 0.6]);
  %caxis([4*10^5 3*10^6]);
  divmap=diverging_map(linspace(0,1,256),[0.23 0.299 0.754],[0.706 0.016 0.15]);
  colormap(divmap);
      
      
      
      
      
      %colormap(cmap);
      hc=colorbar();
      %set(hc,'Ylim',[-4000 5000]);
      %set(hc,'Ylim',[-0.0044 0.0027]);
      
  set(hc,'Ylim',[minval maxval]);
      
       
  print('-djpeg', imfile);
  
  hold off
   
%    clf;
%    close(gcf);
%   clear all;
  
end
  