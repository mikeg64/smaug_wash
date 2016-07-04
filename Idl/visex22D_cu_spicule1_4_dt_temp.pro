cdtarr=dblarr(1)
maxa=fltarr(1)
mina=fltarr(1)
cuta=fltarr(2000,50)




DEVICE, PSEUDO=8, DECOMPOSED=0, RETAIN=2
WINDOW, /FREE, /PIXMAP, COLORS=256 & WDELETE, !D.WINDOW
PRINT, 'Date:      ', systime(0)
PRINT, 'n_colors   ', STRCOMPRESS(!D.N_COLORS,/REM)
PRINT, 'table_size ', STRCOMPRESS(!D.TABLE_SIZE,/REM)

;window, 0,xsize=1200,ysize=700,XPOS = 1000, YPOS = 300 ; ZOOM
;window, 0,ysize=1600,xsize=800,XPOS = 100, YPOS = 300
window, 0,ysize=500,xsize=800,XPOS = 100, YPOS = 300

ii=1



if (ii eq 1) then begin
loadct,4
endif else begin
loadct,0
tek_color
endelse

ipic=long(1)

n1=2048
n2=1024
nsect1=512
nsect2=512

pic=1851
;pic=pic/2

wdtv1=dblarr(pic+1,2)
wdt=dblarr(pic+1,n2,4)
wdt1=dblarr(pic+1,n2,4)

wdtv=dblarr(pic+1,n1,4)
wdt1v=dblarr(pic+1,n1,4)


wfft=dblarr(pic+1,n2,4)
wfftv=dblarr(pic+1,n1,4)
dt=0.001

for ipic=0,pic do begin
;while not(eof(1)) do begin

mass=dblarr(1)
egas=dblarr(1)
tm=dblarr(1)
dtt=dblarr(1)

VV=dblarr(1)
VVa=dblarr(1)

ia=1.0

headline='                                                                               '
it=long(1)
ndim=long(1)
neqpar=long(1)
nw=long(1)
varname='                                                                               '
time=double(1)
dum=long(1)
dumd=long(1)

; Open an MPEG sequence: 
;mpegID = MPEG_OPEN([900,900],FILENAME='myMovie.mpg') 

nn=0


nn_i=0

close,1
close,2


;openr,1,'/data/ap1vf/4mm4mm200Nx255Nz.ini',/f77_unf
;openr,1,'/data/ap1vf/1_8Mnz4Mnx882400.out',/f77_unf

;openr,1,'/data/ap1vf/1_8Mnz4Mnx1983400.ini',/f77_unf

;openr,1,'/data/ap1vf/4Mnzx1976400.ini',/f77_unf

;openr,1,'/data/cs1mkg/VAC_NN_tests/zeroBW_p13.out',/f77_unf
;openr,1,'/home/mikeg/proj/sac2.5d-cuda/zero1_BW_bin.ini',/f77_unf
;openr,1,'/home/mikeg/proj/sac2.5d-cuda/zero1_BW.ini',/f77_unf
;openr,1,'/home/mikeg/proj/sac2.5d-cuda/test_OT.out'
;directory='/home/mikeg/proj/sac2.5d-cuda/out_OT_withhyper/'
;directory='../out/'
;directory='/fastdata/cs1mkg/smaug/spicule1/'
;directory='/fastdata/cs1mkg/smaug/spicule_nob1/'
;directory='/fastdata/cs1mkg/smaug/spicule_nosource_nohydros/'
;directory='/fastdata/cs1mkg/smaug/spicule_nohydros/'
;directory='/fastdata/cs1mkg/smaug/spicule7_nob/'
;directory='/fastdata/cs1mkg/smaug/spicule7a_nob/'
;directory='/fastdata/cs1mkg/smaug/spicule6a_nob/'

;directory='/data/cs1mkg/smaug_spicule1/out/spicule5b4/'
;directory='/fastdata/cs1mkg/smaug/em4b4_bhor120/'
directory='/fastdata/cs1mkg/smaug/spicule6b0_nob_original/'
;pic=999
name='zerospic1__'
;name='zerospic1_'





;ndim=2
;n1=800
;n2=6


;picid=ipic*5+4
;picid=ipic
picid=ipic*1000L
;picid=ipic*2000L
;picid=ipic*500L


;if(picid lt 149500)then begin
;	name='zerospic1_
;endif 
;if( picid ge 149500 && picid le 297000) then begin
;	;name='zerospic1_restart_'
;        name='zerospic1_'       
;endif

;if (picid gt 297000) then begin
;	name='zerospic1_'
;endif


outfile=directory+name+strtrim(string(picid),2)+'.out'
openr,1,outfile
readu,1,headline
readu,1,it,time,ndim,neqpar,nw
gencoord=(ndim lt 0)
;tarr=[tarr,time]
;ndim=abs(ndim)
nx=lonarr(ndim)
readu,1,nx
eqpar=dblarr(neqpar)
readu,1,eqpar
readu,1,varname

print,'varname ',varname


xout=dblarr(2)
yout=dblarr(2)


n1=nx(0)
n2=nx(1)
x=dblarr(n1,n2,ndim)
if (nn eq 0) then w=dblarr(n2,n1,nw)   ;was n1,n2,nw
wi=dblarr(n1,n2)
;e2=dblarr(n1,n2)
readu,1,x
;readu,1,e2
;e2=rotate(e2,1)
for iw=0,nw-1 do begin
 readu,1,wi
 w(*,*,iw)=rotate(wi,1)
endfor

wdtv(ipic,*,0)=w(nsect1,*,0)
wdtv(ipic,*,1)=w(nsect1,*,1)/(w(nsect1,*,0)+w(nsect1,*,7))
wdtv(ipic,*,2)=w(nsect1,*,2)/(w(nsect1,*,0)+w(nsect1,*,7))
wdtv(ipic,*,3)=w(nsect1,*,3)
wdt(ipic,*,0)=w(*,nsect2,0)
wdt(ipic,*,1)=w(*,nsect2,1)/(w(*,nsect2,0)+w(*,nsect2,7))
wdt(ipic,*,2)=w(*,nsect2,2)/(w(*,nsect2,0)+w(*,nsect2,7))
wdt(ipic,*,3)=w(*,nsect2,3)


wdt1v(ipic,*,0)=w(nsect1+256,*,0)
wdt1v(ipic,*,1)=w(nsect1+256,*,1)/(w(nsect1+256,*,0)+w(nsect1+256,*,7))
wdt1v(ipic,*,2)=w(nsect1+256,*,2)/(w(nsect1+256,*,0)+w(nsect1+256,*,7))
wdt1v(ipic,*,3)=w(nsect1+256,*,3)
wdt1(ipic,*,0)=w(*,nsect2+1024,0)/(w(*,nsect2+1024,0)+w(*,nsect2+1024,7))
wdt1(ipic,*,1)=w(*,nsect2+1024,1)/(w(*,nsect2+1024,0)+w(*,nsect2+1024,7))
wdt1(ipic,*,2)=w(*,nsect2+1024,2)
wdt1(ipic,*,3)=w(*,nsect2+1024,3)

wdtv1(ipic,0)=w(511,171,1)/(w(511,171,0)+w(511,171,7))
wdtv1(ipic,1)=w(511,171,2)/(w(511,171,0)+w(511,171,7))
Vt=dblarr(n1,n2)
B=dblarr(n1,n2)
B_bg=dblarr(n1,n2)

p=dblarr(n1,n2,1)
;e2=dblarr(n1,n2)



;!p.multi = [0,1,0,0,1]
;!p.multi = [0,3,2,0,1]
;!p.multi = [0,2,2,0,1]
!p.multi = [0,2,1,0,1]

;!P.multi=0
;if nn eq 1 then stop

;read, aa

;w1=dblarr(n1-4,n2-4,iw)
;w1(0:507,0:507,*)=w(2:509,2:509,*)


mu=4.0*!PI/1.0e7

print,time

kk=100

label_rho='!4q!X'+' ('+'!19kg/m!X!U3'+'!N)'
label_p='p'+' ('+'!19H/m!X!U2'+'!N)'
label_Bx='Bx'
label_By='By'
label_Bz='Bz'


R=8.3e+003
mu=1.257E-6
mu_gas=0.6
gamma=1.66667

;mkg BW test
gamma=2.0
mu=1
xstart=0
xend=511

myrange=[x(0,0,0)/1.0d6,x(n1-1,0,0)/1.0d6]
mxrange=[x(0,0,1)/1.0d6,x(0,n2-1,1)/1.0d6]
mtrange=[0,picid*dt]
mv1range=[-1,1]
mv2range=[-1,1]


Vt(*,*)=sqrt((w(*,*,1)/(w(*,*,0)+w(*,*,7)))^2.0+(w(*,*,2)/(w(*,*,0)+w(*,*,7)))^2.0)

B(*,*)=sqrt((w(*,*,4)*SQRT(mu))^2.0+(w(*,*,5)*SQRT(mu))^2.0)
;B_bg(*,*,*)=sqrt((w1(*,*,*,5)*SQRT(mu))^2.0+(w1(*,*,*,6)*SQRT(mu))^2.0+(w1(*,*,*,7)*SQRT(mu))^2.0)

p(*,*,0)=(gamma-1)*(w(*,*,3)+w(*,*,6)-0.5*((w(*,*,1)*w(*,*,1)+w(*,*,2)*w(*,*,2))/(w(*,*,0)+w(*,*,7)))-0.5*(B(*,*)*B(*,*)))
p(*,*,0)=p(*,*,0)+0.5*B(*,*)*B(*,*)
if (ii eq 1) then begin

;tvframe,reform(w(*,*,1)/(w(*,*,0)+w(*,*,7))),/bar,/sample, title='Vx', xtitle='x', ytitle='z',charsize=2.0    
;tvframe,reform(w(*,*,2)/(w(*,*,0)+w(*,*,7))),/bar,/sample, title='Vy', xtitle='x', ytitle='z',charsize=2.0   



;tvframe,w(*,*,7)+w(*,*,0), /bar,title='log rho_b',/sample, xtitle='x', ytitle='y',charsize=2.0  

;stop
tvframe,w(*,*,1)/(w(*,*,7)+w(*,*,0)), /bar,title='v1',/sample, xtitle='x', ytitle='y',charsize=1.1, xrange=mxrange, yrange=myrange, brange=mv1range  
tvframe,w(*,*,2)/(w(*,*,7)+w(*,*,0)), /bar,title='v2',xtitle='x',/sample, ytitle='z',charsize=1.1, xrange=mxrange, yrange=myrange, brange=mv2range 
;tvframe,w(200:220,120:140,1)/(w(200:220,120:140,7)+w(200:220,120:140,0)), /bar,title='v1',/sample, xtitle='x', ytitle='y',charsize=2.0  
;tvframe,w(200:220,120:140,2)/(w(200:220,120:140,7)+w(200:220,120:140,0)), /bar,title='v2',xtitle='x',/sample, ytitle='z',charsize=2.0 


;tvframe,w(*,*,1), /bar,title='v1',/sample, xtitle='x', ytitle='y',charsize=2.0  
;tvframe,w(*,*,2), /bar,title='v2',xtitle='x',/sample, ytitle='z',charsize=2.0 
;;tvframe,w(*,*,3)+w(*,*,6),/bar,/sample, title='e', xtitle='x', ytitle='z', charsize=2.0 
;tvframe,w(*,*,3)*1.0d7,/bar,/sample, title='e (X1.0d7)', xtitle='x', ytitle='z', charsize=1.1, xrange=myrange, yrange=mxrange                                                                                                   

;;tvframe,w(*,*,6),/bar,/sample, title='eb',  xtitle='x', ytitle='z', charsize=2.0
;tvframe,w(*,*,7)+w(*,*,0), /bar,title='log rho_b',/sample, xtitle='x', ytitle='y',charsize=2.0
;tvframe,w(*,*,0)*1.0d14,/bar,/sample, title='rho (X1.0d14)',  xtitle='x', ytitle='z', charsize=1.1, xrange=myrange, yrange=mxrange

;;;tvframe,w(*,*,4),/bar,/sample, title='b_z',  xtitle='x', ytitle='z', charsize=2.0, xrange=mxrange, yrange=myrange, brange=mv1range
;;;tvframe,w(*,*,5),/bar,/sample, title='b_x',  xtitle='x', ytitle='z', charsize=2.0, xrange=mxrange, yrange=myrange, brange=mv2range
;tvframe,w(*,*,4)+w(*,*,8),/bar,/sample, title='b_z',  xtitle='x', ytitle='z', charsize=2.0
;tvframe,w(*,*,5)+w(*,*,9),/bar,/sample, title='b_x',  xtitle='x', ytitle='z', charsize=2.0
;tvframe,w(*,*,4),/bar,/sample, title='b_z',  xtitle='x', ytitle='z', charsize=2.0
;tvframe,w(*,*,5),/bar,/sample, title='b_x',  xtitle='x', ytitle='z', charsize=2.0
;tvframe,w(*,*,8),/bar,/sample, title='bg_z',  xtitle='x', ytitle='z', charsize=2.0
;tvframe,w(*,*,9),/bar,/sample, title='bg_x',  xtitle='x', ytitle='z', charsize=2.0

;plot, w(*,10,0), title='rho', charsize=2.0
;oplot, w(*,10,0), psym=4
;plot, w(*,10,1), title='v1'
;oplot, w(*,10,1), psym=4
;plot, w(*,10,2), title='v2'
;oplot, w(*,10,2), psym=4
;plot, w(*,10,3), title='e'
;oplot, w(*,10,3), psym=4
;plot, w(*,10,4), title='b1'
;oplot, w(*,10,4), psym=4
;plot, w(*,10,5), title='b2'
;oplot, w(*,10,5), psym=4
;stop

t=3
;plot, w(t,*,0), title='rho', charsize=2.0
;oplot, w(t,*,0), psym=4
;plot, w(t,*,1)/(w(t,*,0)+w(t,*,7)), title='v1', charsize=2.0
;oplot, w(t,*,1)/(w(t,*,0)+w(t,*,7)), psym=4
;plot, w(t,*,2)/(w(t,*,0)+w(t,*,7)), title='v2', charsize=2.0
;oplot, w(t,*,2)/(w(t,*,0)+w(t,*,7)), psym=4
;plot, w(t,*,3), title='e', charsize=2.0
;oplot, w(t,*,3), psym=4
;plot, w(t,*,4), title='b1', charsize=2.0
;oplot, w(t,*,4), psym=4
;plot, p(*,t,0), title='p', charsize=2.0
;oplot, p(*,t,0), psym=4
;plot, w(t,*,5), title='b2', charsize=2.0
;oplot, w(t,*,5), psym=4
;stop
endif else begin

;plot, (w(kk1:kk2,*,1)/(w(kk1:kk2,*,0)+w(kk1:kk2,*,7))),title='Vx', xtitle='x', ytitle='z',charsize=2.0 ;, psym=3
;plot, (w(kk1:kk2,*,2)/(w(kk1:kk2,*,0)+w(kk1:kk2,*,7))),title='Vy', xtitle='x', ytitle='z',charsize=2.0   


;surface,w(*,*,0)

x1=0
x2=399

kk1=4
kk2=4

;plot, (w(kk1:kk2,x1:x2,0)+w(kk1:kk2,x1:x2,7)),title='rho+rhoB', xtitle='x', ytitle='y',charsize=2.0, /ys  ,/xs,/ylog
;oplot,(w(kk1:kk2,x1:x2,0)+w(kk1:kk2,x1:x2,7)),psym=4,color=3

plot, (w(kk1:kk2,x1:x2,0)),title='rho', xtitle='x', ytitle='y',charsize=2.0, /ys  ,/xs
oplot,(w(kk1:kk2,x1:x2,0)),psym=4,color=7

;(w(kk1:kk2,x1:x2,1)/(w(kk1:kk2,x1:x2,0)+w(kk1:kk2,x1:x2,7)))
plot, w(kk1:kk2,x1:x2,1)/(w(kk1:kk2,x1:x2,0)+w(kk1:kk2,x1:x2,7)),title='v1', xtitle='x', ytitle='y',charsize=2.0 ,/ys ,/xs
oplot,w(kk1:kk2,x1:x2,1)/(w(kk1:kk2,x1:x2,0)+w(kk1:kk2,x1:x2,7)),psym=4,color=2
plot, (w(kk1:kk2,x1:x2,2)/(w(kk1:kk2,x1:x2,0)+w(kk1:kk2,x1:x2,7))), title='v2',xtitle='x', ytitle='z',charsize=2.0 ,/ys,/xs
oplot,(w(kk1:kk2,x1:x2,2)/(w(kk1:kk2,x1:x2,0)+w(kk1:kk2,x1:x2,7))),psym=4,color=6


plot, (w(kk1:kk2,x1:x2,3)),title='e', xtitle='x', ytitle='y',charsize=2.0,/xs ;,psym=3
oplot,(w(kk1:kk2,x1:x2,3)),psym=4,color=6

plot, w(kk1:kk2,x1:x2,6)+w(kk1:kk2,x1:x2,3), title='eb+e', xtitle='x', ytitle='z', charsize=2.0   ,/xs 
oplot, w(kk1:kk2,x1:x2,6)+w(kk1:kk2,x1:x2,3),psym=5,color=5


plot, (w(kk1:kk2,x1:x2,7)), title='rhob', xtitle='x', ytitle='z', charsize=2.0, /ys    ,/xs

plot, w(kk1:kk2,x1:x2,6)+w(kk1:kk2,x1:x2,3), title='e_T', xtitle='x', ytitle='z', charsize=2.0   ,/xs 


plot, w(kk1:kk2,x1:x2,5),title='By', xtitle='x', ytitle='y',charsize=2.0, /ys  ,/xs
oplot,w(kk1:kk2,x1:x2,5),psym=4,color=3
print,'endelse'

endelse


tt:

T=dblarr(n2,n1)


;T[*,*]=w[*,*,3]+w[*,*,6]


;T[*,*]=T[*,*]-(w[*,*,1]^2.0+w[*,*,2]^2.0)/(w[*,*,0]+w[*,*,7])/2.0

;T[*,*]=T[*,*]-(w[*,*,4]^2.0+w[*,*,5]^2.0)/2.0


B=dblarr(n2,n1)

B[*,*]=sqrt(((w[*,*,8]+w[*,*,4])^2.0+(w[*,*,9]+w[*,*,5])^2.0))

;tvframe,B,/bar,/sample, title='B',  xtitle='x', ytitle='z', charsize=2.0

beta=dblarr(n2,n1)
print,'computing beta'
;beta[*,*]=((B[*,*]*sqrt(mu)*1.0e4)^2.0)/2.0/((gamma-1.d0)*T[*,*])


;plot, alog10(1.d0/beta[200,*]),title='beta',xtitle='x', ytitle='z',charsize=2.0 

print,'reforming'
C=dblarr(n2,n1)
;C[*,*]=sqrt(gamma*T[*,*]/(reform(w[*,*,0]+w[*,*,7])))


Va=dblarr(n2,n1)
;Va[*,*]=B[*,*]/(sqrt(reform(w[*,*,0]+w[*,*,7])))


;T[*,*]=mu_gas*(gamma-1.d0)*T[*,*]/R/(w[*,*,0]+w[*,*,7])


;tvframe,C,/bar,/sample, title='Cs',  xtitle='x', ytitle='z', charsize=2.0
;tvframe,Va,/bar,/sample, title='Va',  xtitle='x', ytitle='z', charsize=2.0



;!P.multi=[1,3,0,0,1]
;for i=0,1900 do begin
;plot, C(*,i), yrange=[10000, 120000], charsize=2

;oplot, Va(*,i),  psym=4 
;wait, 0.002
;print, x(i,1,0)/1.d6,'  ',i
;if i eq 0 then begin
;VV[i]=min(C(*,i))/max(C(*,i))
;VVa[i]=min(Va(*,i))/max(Va(*,i))
;endif else begin
;VV=[VV,min(C(*,i))/max(C(*,i))]
;VVa=[VVa,min(Va(*,i))/max(Va(*,i))]
;endelse
;plot, VV, psym=4, title='CC', charsize=2
;plot,VVa,psym=3, title='VaVa', charsize=2

;endfor


;set_plot, 'ps' 

;file_name='Cmin-Cmax.eps'
;device, filename=file_name, /ENCAPSULATED, BITS=8, /color, xsize=12, ysize=10
; !P.multi=0

;!p.thick = 2
;!x.thick = 2
;!y.thick = 2
;!z.thick = 2


;plot, x(*,1,0)/1.d6, VV(*), xtitle='z [Mm]', yrange=[0.6, 1.2],ytitle='C!Bmin!N/C!Bmax!N',charsize=1.d0

;device, /close
;set_plot, 'x'
;print, 'ps complete'
;stop

;tvframe,rotate(beta(*,*,pp),1),/bar,/sample, title='1/beta',  xtitle='x', ytitle='z', charsize=2.0

;plot, alog10(T(kk,*)),title='T', xtitle='x', ytitle='z',charsize=3.0 

;tek_color

;if (ii eq 1) then loadct,4

;tvframe,reform(T(*,*)), /bar,title='T',xtitle='x',/sample, ytitle='z',charsize=2.0 

;stop

a=''

nn=nn+1

if (ia eq 1) then begin
 tm(0)=time
 mass(0)=total(w(*,*,7)+w(*,*,0)) 
 egas(0)=total(w(*,*,3)+w(*,*,6))
 ia=2.0
endif else begin
 tm=[tm,time]
 mass=[mass,total(w(*,*,7)+w(*,*,0))] 
 egas=[egas,total(w(*,*,3)+w(*,*,6))]
endelse

;plot,mass, charsize=2.0, ystyle=1, title='mass'
;plot,egas, charsize=2.0, ystyle=1, title='egas'

indexs=strtrim(nn,2)

 ss='time ='+strTrim(string(time),1)+' it ='+strTrim(string(it),1)+'  nn = '+strTrim(string(nn),1)
 xyouts,50,2, ss, /device, color=200
;if (ii eq 2) then read,a

;maxa=[maxa,max(w(*,*,2)/(w(*,*,0)+w(*,*,7)))]
maxa=[maxa,max(Vt)]


;indexs=strtrim(nn,2)
indexs=strtrim(ipic,2)
a = strlen(indexs)                                                  
case a of                                                           
 1:indexss='0000'+indexs                                             
 2:indexss='000'+indexs                                              
 3:indexss='00'+indexs                                               
 4:indexss='0'+indexs                                               
endcase   

image_p = TVRD_24()
write_png,'/data/cs1mkg/smaug_spicule1/Idl/images/spic6b0/pmode150s_sindriver_n0_6b0_'+indexss+'.png',image_p, red,green, blue
;stop
;endwhile
close,1
endfor

tvframe,wdt(*,*,1), /bar,title='v1',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 
tvframe,wdt(*,*,2), /bar,title='v2',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 
;tvframe,wdt(*,*,0), /bar,title='Density (X 1.0d14)',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 
;tvframe,wdt(*,*,3), /bar,title='Energy (X 1.0d7)',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 




image_p = TVRD_24()
write_png,'/data/cs1mkg/smaug_spicule1/Idl/images/spic6b0/pmode150s_sindriver_n0_6b0_1p5Mm_hdt.png',image_p, red,green, blue




tvframe,wdt1v(*,0:550,1), /bar,title='v1',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=myrange 
tvframe,wdt1v(*,0:550,2), /bar,title='v2',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=myrange 
;tvframe,wdt1(*,*,0), /bar,title='Density (X 1.0d14)',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 
;tvframe,wdt1(*,*,3), /bar,title='Energy (X 1.0d7)',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 




image_p = TVRD_24()
write_png,'/data/cs1mkg/smaug_spicule1/Idl/images/spic6b0/pmode150s_sindriver_n0_6b0_2Mm_vtrandt.png',image_p, red,green, blue









tvframe,wdt1(*,*,1), /bar,title='v1',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 
tvframe,wdt1(*,*,2), /bar,title='v2',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 
;tvframe,wdt1(*,*,0), /bar,title='Density (X 1.0d14)',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 
;tvframe,wdt1(*,*,3), /bar,title='Energy (X 1.0d7)',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 




image_p = TVRD_24()
write_png,'/data/cs1mkg/smaug_spicule1/Idl/images/spic6b0/pmode150s_sindriver_n0_6b0_4p5Mm_hdt.png',image_p, red,green, blue



tvframe,wdt1v(*,*,1), /bar,title='v1',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=myrange 
tvframe,wdt1v(*,*,2), /bar,title='v2',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=myrange 
;tvframe,wdt1(*,*,0), /bar,title='Density (X 1.0d14)',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 
;tvframe,wdt1(*,*,3), /bar,title='Energy (X 1.0d7)',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 




image_p = TVRD_24()
write_png,'/data/cs1mkg/smaug_spicule1/Idl/images/spic6b0/pmode150sindriver_n0_6b0_3Mm_vdt.png',image_p, red,green, blue


save,wdt1v,filename='wdt1v_6b0.dat'
save,wdtv1,filename='wdtv1_6b0.dat'

for i=1,n1-1 do begin

   wfft(*,i,0)=fft(wdtv(*,i,0))
   wfft(*,i,1)=fft(wdtv(*,i,1))
   wfft(*,i,2)=fft(wdtv(*,i,2))
   wfft(*,i,3)=fft(wdtv(*,i,3))


endfor

tvframe,wfft(*,*,1), /bar,title='v1',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=myrange 
tvframe,wfft(*,*,2), /bar,title='v2',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=myrange 
;tvframe,wfft(*,*,0), /bar,title='Density (X 1.0d14)',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 
;tvframe,wfft(*,*,3), /bar,title='Energy (X 1.0d7)',/sample, xtitle='dt (sec)', ytitle='Height (Mm)',charsize=1.1, xrange=mtrange, yrange=mxrange 




image_p = TVRD_24()
write_png,'/data/cs1mkg/smaug_spicule1/Idl/images/spic6b0/spic_fft.png',image_p, red,green, blue


end
