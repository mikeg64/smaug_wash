
%% Determination of Driver Wave Amplitudes for Hydrodynamical Simulations of Pmodes in the Solar Atmosphere
% The amplitude for the n m mode is given by.


%%
% 
% $$  A_{nm}=\frac{2(2T_0-1)}{(2T_i-1)(n^2+m^2+2(n+m)+2)}$$
% 

%% Frequency Computation
%  The series for the normal modes are calculated from the following expressions 
%  for a given of the speed of sound c and a 
%  value for the length of the simulation box of 4Mm. The frequency is computed using
%
% $$ \omega^2=2 \left( \frac{\pi c_s}{L} \right)^2  $$ 
%
% For the normal modes the wave numbers and frequencies satisfy the
% following relationship
%
% $$ \frac{\omega}{k}=c_s $$

%% Table of Amplitudes
% For sound speed 13km/s

%%
% 
% <html>
% <table border="1" style="width: 100%;">
%   <tbody>
% <tr>
%     <td>Mode</td> 
%     <td>Driver Period (s)</td> 
%     <td>Amplitude (m/s)</td>
%     <td>Label</td>
%   </tr>
% <tr>
%     <td>(0,0)</td> 
%     <td>435.1</td>
%     <td>250</td>
%    <td>spicule_4p35_0_0_3d</td>
%   </tr>
% <tr>
%     <td>(0,1)</td> 
%     <td>307.7</td>
%     <td>141.4713</td>
%   <td>spicule3p07a_0_1_3d</td>
%   </tr>
% <tr>
%     <td>(0,2)</td> 
%     <td>205.1</td>
%     <td>70.7357</td>
%   <td>spicule2p05_0_2_3d</td>
%   </tr>
% <tr>
%     <td>(0,3)</td> 
%     <td>153.8</td>
%     <td>41.60921</td>
%   <td>spicule1p53a_0_3_3d</td>
%   </tr>
% </tbody></table>
% </html>
% 

%%
%%
% for 30, 180,300s drivers
% 30s driver  sound speed 188.6km/s

%%
% <html>
% <table border="1" style="width: 100%;">
%   <tbody>
% <tr>
%     <td>Mode</td> 
%     <td>Driver Period (s)</td> 
%     <td>Amplitude (m/s)</td>
%     <td>Label</td>
%   </tr>
% <tr>
%     <td>(0,0)</td> 
%     <td>30.0</td>
%     <td>3683.05</td>
%     <td>spicule4b0_3d</td>
%   </tr>
% <tr>
%     <td>(0,1)</td> 
%     <td>30.0</td>
%     <td>1473.2</td>
%     <td>spic4b0_1_3d</td>
%   </tr>
% <tr>
%     <td>(0,2)</td> 
%     <td>30.0</td>
%     <td>736.61</td>
%     <td>spic4b0_2_3d</td>
%   </tr>
% <tr>
%     <td>(0,3)</td> 
%     <td>30.0</td>
%     <td>433.3</td>
%     <td>spic4b0_3_3d</td>
%   </tr>
% </tbody></table>
% </html>
% 
%%
% 180s driver  sound speed 31.4km/s

%%
% 
% <html>
% <table border="1" style="width: 100%;">
%   <tbody>
% <tr>
%     <td>Mode</td> 
%     <td>Driver Period (s)</td> 
%     <td>Amplitude (m/s)</td>
%     <td>Label</td>
%   </tr>
% <tr>
%     <td>(0,0)</td> 
%     <td>180.0</td>
%     <td>605.29</td>
%     <td>spic6b0_3d</td>
%   </tr>
% <tr>
%     <td>(0,1)</td> 
%     <td>180.0</td>
%     <td>242.116</td>
%     <td>spic6b0_1_3d</td>
%   </tr>
% <tr>
%     <td>(0,2)</td> 
%     <td>180.0</td>
%     <td>121.06</td>
%     <td>spic6b0_2_3d</td>
%   </tr>
% <tr>
%     <td>(0,3)</td> 
%     <td>180.0</td>
%     <td>71.21</td>
%     <td>spic6b0_3_3d</td>
%   </tr>
% </tbody></table>
% </html>
%
%% 
% 300s driver  sound speed 18.9km/s
%%
% 
% <html>
% <table border="1" style="width: 100%;">
%   <tbody>
% <tr>
%     <td>Mode</td> 
%     <td>Driver Period (s)</td> 
%     <td>Amplitude (m/s)</td>
%     <td>Label</td>
%   </tr>
% <tr>
%     <td>(0,0)</td> 
%     <td>300.0</td>
%     <td>362.7712</td>
%     <td>spic5b0_3d</td>
%   </tr>
% <tr>
%     <td>(0,1)</td> 
%     <td>300.0</td>
%     <td>145.1085</td>
%     <td>spic5b0_1_3d</td>
%   </tr>
% <tr>
%     <td>(0,2)</td> 
%     <td>300.0</td>
%     <td>75.5542</td>
%     <td>spic5b0_2_3d</td>
%   </tr>
% <tr>
%     <td>(0,3)</td> 
%     <td>300.0</td>
%     <td>42.679</td>
%     <td>spic5b0_3_3d</td>
%   </tr>
% </tbody></table>
% </html>
% 






function amplitude=pamplitudet(n,m,t0,ti,a00)
    amplitude=2.*a00.*(2.*t0-1)./((2.*ti-1).*(n.^2+m.^2+2.*(n+m)+2) );



 






