%Totall flux in corona, transition and chrmosphere


%first index is period column is mode
efluxcoronaavg=zeros(6,4);
efluxtranavg=zeros(6,4);
efluxchromavg=zeros(6,4);

%20,42,90,117
ef1Mm=zeros(6,4);  %20
ef2Mm=zeros(6,4);  %42
ef4Mm=zeros(6,4);  %90
ef5p5Mm=zeros(6,4); %117


%arrays storing flux values for (1,1) (2,2) (3,3) normal modes
% periods(471.4, 235.7, 157.1 )
%first index is period column is mode
efluxcoronaavgnd=zeros(1,3);
efluxtranavgnd=zeros(1,3);
efluxchromavgnd=zeros(1,3);

%20,42,90,117
ef1Mmnd=zeros(1,3);  %20
ef2Mmnd=zeros(1,3);  %42
ef4Mmnd=zeros(1,3);  %90
ef5p5Mmnd=zeros(1,3); %117


%(0,0) mode
efluxcoronaavgnd(:)=[665.303;0 ;0];
efluxtranavgnd(:)=[4.3055e6;0 ;0 ];
efluxchromavgnd(:)=[1.2648e6;0 ;0 ];

%20,42,90,117
ef1Mmnd(:)=[7.2224e4;0 ;0 ];
ef2Mmnd(:)=[432.3633;0 ;0 ];
ef4Mmnd(:)=[0.7576;0 ;0 ];
ef5p5Mmnd(:)=[0.1869;0 ;0 ];


periodvalues=zeros(6,4);
freqvalues=zeros(6,4);
mode=zeros(4);

mode=[0 1 2 3];

%period values for different modes
%periodvalues=zeros(5,4);
periodvalues(:,1)=[30;300; 180; 435.1;179.98;282.84];  %0,0 mode
periodvalues(:,2)=[30;300;180;307.1;127.27;200.0];    %0,1 mode
periodvalues(:,3)=[30;300;180;205.1;84.84;133.33];   %0,2 mode
periodvalues(:,4)=[30;300;180;153.8;63.63;100.0];   %0,3 mode

freqvalues=2*pi./periodvalues;
freqvalues=freqvalues.*1000;
f1=freqvalues(:,1);
f2=freqvalues(:,2);
f3=freqvalues(:,3);
f4=freqvalues(:,4);

%(0,0) mode
efluxcoronaavg(:,1)=[542.5186; 1.4353e5; 7.832e6 ;2.6811e4 ; 7.8956e6; 7.9381e4];
efluxtranavg(:,1)=[5.0191e4; 3.7837e7;1.6758e9  ;2.1546e7 ; 9.0611e7;  1.1122e7];
efluxchromavg(:,1)=[2.9484e5; -1.0457e7;5.9853e7  ;-8.7572e6 ; 1.2814e7; -4.8432e6];

%20,42,90,117
ef1Mm(:,1)=[860.1025 ;2.05e5 ;3.4511e6  ;9.9591e4 ; 6.2586e6; 1.0498e5 ];
ef2Mm(:,1)=[11.1565 ; 6.4033e3; 2.2871e5  ;2.2365e3 ; 1.7128e4; 2.118e3 ];
ef4Mm(:,1)=[6.8201 ; 1.7107e3; 9.4697e4  ;304.8928 ; 9.8941e3; 975.1936 ];
ef5p5Mm(:,1)=[3.5777; 879.9814;4.9497e4  ; 161.4294; 5.1971e3; 517.0635 ];

%(0,1) mode
efluxcoronaavg(:,2)=[14.5618 ;1.5449e3 ;8.4186e3 ;1.5714e3 ;1.2199e4 ;6.0716e3 ];
efluxtranavg(:,2)=[ 3.7958e3 ;6.1873e6 ;5.3804e6 ;9.2829e6 ; 4.3103e6; 4.1602e6];
efluxchromavg(:,2)=[ 1.2457e5  ;1.1965e5 ;5.7499e6 ;-1.839e5 ;5.5082e6 ;4.0662e6 ];

%300;180;425.9;307.1;127.27;200.0
%20,42,90,117
ef1Mm(:,2)=[ 512.2253 ;9.4785e4 ;2.7138e5 ;8.8814e4 ; 1.5255e5; 1.9914e5 ];
ef2Mm(:,2)=[1.3725  ;832.4453 ;1.0268e3 ;920.2316 ;794.994 ; 781.058];
ef4Mm(:,2)=[ 0.0986 ;3.928 ;57.5391 ;3.7417 ; 94.5877;35.6865 ];
ef5p5Mm(:,2)=[ 0.0367 ;1.2362 ;19.9496 ;1.2107 ;37.5449 ; 11.1488];

%(0,2) mode
efluxcoronaavg(:,3)=[ 6.215 ;1.3243e3 ;9.9477e3 ;4.9909e3 ;1.2757e3 ;1.1309e4 ];
efluxtranavg(:,3)=[ 2.8547e3 ;7.0522e6 ;3.774e6 ;2.4807e6 ;3.0096e5 ;2.0328e6 ];
efluxchromavg(:,3)=[ 5.8686e4 ;1.6222e6;3.302e6 ;2.5583e6  ;1.2301e6 ;2.7962e6 ];

%300;180;301.25;205.1;84.84;133.33
%20,42,90,117
ef1Mm(:,3)=[166.2611  ;8.1059e4 ;1.3882e5 ;1.1077e5 ;1.9653e4 ; 8.9183e4 ];
ef2Mm(:,3)=[0.4932  ;695.0993 ;718.7246 ;532.5383 ; 56.2573; 354.1246 ];
ef4Mm(:,3)=[0.0728  ;7.7937 ;122.6795 ;58.3634 ; 15.7784; 143.2859 ];
ef5p5Mm(:,3)=[ 0.052 ;5.8724 ;83.8924 ;39.8216 ; 11.3557; 100.9888 ];




%(0,3) mode
efluxcoronaavg(:,4)=[ 520.6026;590.5835  ;839.2984 ;867.6703 ;37.4092 ;370.3021 ];
efluxtranavg(:,4)=[2.12e3;3.8737e6   ;1.7327e6 ;9.03e5 ;2.7312e4 ; 1.9133e5];
efluxchromavg(:,4)=[ 1.327e7;1.7685e6  ;2.2274e6 ;1.9359e6 ;3.4941e5 ; 1.0820e6];

%300;180;231.0;153.8;63.63;100.0
%20,42,90,117
ef1Mm(:,4)=[ 106.6359;6.6236e4  ;8.2435e4 ;6.4222e4 ;2.6508e3 ; 1.9760e4 ];
ef2Mm(:,4)=[ 0.4524;717.814  ;327.9077 ;226.2774 ;5.1224 ;  40.1447];
ef4Mm(:,4)=[ 0.0067;0.6015  ;7.3686 ;7.8008 ; 0.3633; 3.7331];
ef5p5Mm(:,4)=[ 0.004;0.392  ;4.2801 ;4.3098 ; 0.2102;  2.1863];

f1=freqvalues(:,1);
f2=freqvalues(:,2);
f3=freqvalues(:,3);
f4=freqvalues(:,4);

efc1=ef5p5Mm(:,1);
efc2=ef5p5Mm(:,2);
efc3=ef5p5Mm(:,3);
efc4=ef5p5Mm(:,4);

a(1)=0.4733;
b(1)=0.3517;
c(1)=-5.105e5;
d(1)=-1.936;
e(1)=7513;
f(1)=3.842e5;

delta=(200-15)/20;
f1fit1=15:delta:200;
fitval1=a(1).*exp(-b(1).*(f1fit1.^2))+c(1).*(f1fit1.^(-0.1))+d(1).*f1fit1.^2+f(1);


a(4)=0.4505;
b(4)=0.08382;
c(4)=-1.534;
d(4)=-6.894e-5;
e(4)=7513;
f(4)=3.621;

f1fit4=15:delta:200;
fitval4=a(4).*exp(-b(4).*(f1fit4.^2))+c(4).*(f1fit4.^(-0.1))+d(4).*f1fit4.^2+f(4);





%plot(periodvalues(1:7,1),ef5p5Mm(1:7,1),'o',periodvalues(1:7,2),ef5p5Mm(1:7,2),'+',periodvalues(1:7,3),ef5p5Mm(1:7,3),'x',periodvalues(1:7,4),ef5p5Mm(1:7,4),'s');
%semilogy(periodvalues(1:6,1),ef5p5Mm(1:6,1),'o',periodvalues(1:6,2),ef5p5Mm(1:6,2),'+',periodvalues(1:6,3),ef5p5Mm(1:6,3),'x',periodvalues(1:6,4),ef5p5Mm(1:6,4),'s');
%semilogy(periodvalues(1:6,1),(efluxcoronaavg(1:6,1)+0.01),'o',periodvalues(1:6,2),(efluxcoronaavg(1:6,2)+0.01),'+',periodvalues(1:6,3),(efluxcoronaavg(1:6,3)+0.01),'x',periodvalues(1:6,4),(efluxcoronaavg(1:6,4)+0.01),'s');

%semilogy(freqvalues(1:6,1),ef5p5Mm(1:6,1),'o',freqvalues(1:6,2),ef5p5Mm(1:6,2),'+',freqvalues(1:6,3),ef5p5Mm(1:6,3),'x',freqvalues(1:6,4),ef5p5Mm(1:6,4),'s');
%loglog(freqvalues(1:6,1),ef5p5Mm(1:6,1),'o',freqvalues(1:6,2),ef5p5Mm(1:6,2),'+',freqvalues(1:6,3),ef5p5Mm(1:6,3),'x',freqvalues(1:6,4),ef5p5Mm(1:6,4),'s');
plot(log10(freqvalues(1:6,1)),log10(ef5p5Mm(1:6,1)),'o',log10(freqvalues(1:6,2)),log10(ef5p5Mm(1:6,2)),'+',log10(freqvalues(1:6,3)),log10(ef5p5Mm(1:6,3)),'x',log10(freqvalues(1:6,4)),log10(ef5p5Mm(1:6,4)),'s');
hold on;
plot(log10(f1fit1),log10(fitval1));

plot(log10(f1fit4),log10(fitval4));

