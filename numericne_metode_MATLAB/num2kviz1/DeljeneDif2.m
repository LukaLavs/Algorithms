function d = DeljeneDif2(X, Y, dY)
% Funkcija izračuna koeficiente Newtonovega interpolacijskega polinoma
% z metodo deljenih diferenc za Hermitovo interpolacijo.
%
% Vhod:
% X  - vektor vozlišč (n x 1)
% Y  - vektor vrednosti funkcije v vozliščih (n x 1)
% dY - vektor vrednosti odvoda funkcije v vozliščih (n x 1)
%
% Izhod:
% d  - vektor koeficientov deljenih diferenc

n = length(X);
Z = zeros(2*n, 1); % podvojena vozlišča
Q = zeros(2*n, 2*n); % tabela deljenih diferenc

% Zapolni podvojena vozlišča in prvi stolpec tabele
for i = 1:n
    Z(2*i-1) = X(i);
    Z(2*i) = X(i);
    Q(2*i-1, 1) = Y(i);
    Q(2*i, 1) = Y(i);
    Q(2*i, 2) = dY(i); % odvod
    if i ~= 1
        Q(2*i-1, 2) = (Q(2*i-1,1) - Q(2*i-2,1)) / (Z(2*i-1) - Z(2*i-2));
    end
end

% Računanje ostalih deljenih diferenc
for j = 3:2*n
    for i = j:2*n
        Q(i,j) = (Q(i,j-1) - Q(i-1,j-1)) / (Z(i) - Z(i-j+1));
    end
end

% Koeficienti so prvi elementi vsakega stolpca
d = diag(Q);
end