 %uuinterp=triinterp(scx(),scy(),scz(),uu,x1,x2,x3);
%http://en.wikipedia.org/wiki/Trilinear_interpolation
%xval is the value of x at which we wish to interpolate
%f is the series of values
function y=triinterp(sx,sy,sz,uu,xa1,ya1,za1)  
    
x=sx;
y=sy;
z=sz;


if(int32(x)>x)
    ix0=int32(x);
    ix1=ix0+1;
else
    ix0=int32(x);
    ix1=ix0+1;
end

if(int32(y)>y)
    iy0=int32(y);
    iy1=iy0+1;
else
    iy0=int32(y);
    iy1=iy0+1;
end


if(int32(z)>z)
    iz0=int32(z);
    iz1=iz0+1;
else
    iz0=int32(z);
    iz1=iz0+1;
end

xd=(x-xa1(ix0,iy0,iz0))/(xa1(ix1,iy1,iz1)-xa1(ix0,iy0,iz0));
yd=(y-ya1(ix0,iy0,iz0))/(ya1(ix1,iy1,iz1)-ya1(ix0,iy0,iz0));
zd=(z-za1(ix0,iy0,iz0))/(za1(ix1,iy1,iz1)-za1(ix0,iy0,iz0));


c00=uu(ix0,iy0,iz0)*(1-xd)+uu(ix1,iy0,iz0)*xd;
c10=uu(ix0,iy1,iz0)*(1-xd)+uu(ix1,iy1,iz0)*xd;
c01=uu(ix0,iy0,iz1)*(1-xd)+uu(ix1,iy0,iz1)*xd;
c11=uu(ix0,iy1,iz1)*(1-xd)+uu(ix0,iy1,iz1)*xd;

c0=c00*(1-yd)+c10*yd;
c1=c01*(1-yd)+c11*yd;

y=c0*(1-zd)+c1*zd;
   



%endfunction
