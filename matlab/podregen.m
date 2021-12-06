%use pod analysis to reconstruct fields from the pod coefficients


k = 100; % for example
nt=1625;
Utilde_k_s = A_s(:,k)*PHI_s(:,k)';
% Normalization to match direct and snapshot modes (optional)
PHI = normc(PHI_s); % Spatial modes
A = U*PHI; % Time coefficients
Utilde_k = A(:,k)*PHI(:,k)'; % Reconstruction on mode k


st=reshape(Utilde_k,[nt,124,124]);
subplot(1,4,1)
s1=surf(reshape(st(90,:,:),[124,124]));
s1.EdgeColor = 'none';
view(2);


k = 105; % for example
Utilde_k_s = A_s(:,k)*PHI_s(:,k)';
% Normalization to match direct and snapshot modes (optional)
PHI = normc(PHI_s); % Spatial modes
A = U*PHI; % Time coefficients
Utilde_k = A(:,k)*PHI(:,k)'; % Reconstruction on mode k


st=reshape(Utilde_k,[nt,124,124]);
subplot(1,4,2)
s2=surf(reshape(st(90,:,:),[124,124]));
s2.EdgeColor = 'none';
view(2);


k = 110; % for example
Utilde_k_s = A_s(:,k)*PHI_s(:,k)';
% Normalization to match direct and snapshot modes (optional)
PHI = normc(PHI_s); % Spatial modes
A = U*PHI; % Time coefficients
Utilde_k = A(:,k)*PHI(:,k)'; % Reconstruction on mode k


st=reshape(Utilde_k,[nt,124,124]);
subplot(1,4,3)
s3=surf(reshape(st(90,:,:),[124,124]));
s3.EdgeColor = 'none';
view(2);


k = 1; % for example
Utilde_k_s = A_s(:,k)*PHI_s(:,k)';
% Normalization to match direct and snapshot modes (optional)
PHI = normc(PHI_s); % Spatial modes
A = U*PHI; % Time coefficients
Utilde_k = A(:,k)*PHI(:,k)'; % Reconstruction on mode k


st=reshape(Utilde_k,[nt,124,124]);
subplot(1,4,4)
s4=surf(reshape(st(90,:,:),[124,124]));
s4.EdgeColor = 'none';
view(2);


