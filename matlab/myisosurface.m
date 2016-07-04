%use plotsecs_iso_array to load data and set values

maxv=max(max(max(umag)));
minv=min(min(min(umag)));


isovalue=maxv;
     fv = patch(isosurface(x1,x2,x3,umag,isovalue));
      isonormals(x1,x2,x3,umag,fv)
     set(fv,'FaceColor','red','EdgeColor','none'); 
  hold on;   
     
isovalue=minv;
     fv = patch(isosurface(x1,x2,x3,umag,isovalue));
      isonormals(x1,x2,x3,umag,fv)
     set(fv,'FaceColor','blue','EdgeColor','none');      
 hold on;    
     
 
 isovalue=minv+(maxv-minv)/2;
     fv = patch(isosurface(x1,x2,x3,umag,isovalue));
      isonormals(x1,x2,x3,umag,fv)
     set(fv,'FaceColor','green','EdgeColor','none');      
 hold on; 
 
 
      daspect([1,1,1])
view(3); 
axis tight;
camlight; 
lighting gouraud ;