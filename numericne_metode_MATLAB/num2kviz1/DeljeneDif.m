function d = deljeneDif(X, Y)
% Funkcija izračuna koeficiente Newtonovega interpolacijskega polinoma
% z metodo deljenih diferenc.
%
% Vhod:
% X - vektor vozlišč
% Y - vektor vrednosti funkcije v vozliščih
%
% Izhod:
% d - vektor koeficientov deljenih diferenc

n = length(X);
D = zeros(n, n); % tabela deljenih diferenc

% Prvi stolpec so funkcijske vrednosti
D(:,1) = Y(:);

% Računanje deljenih diferenc
for j = 2:n
    for i = j:n
        D(i,j) = (D(i,j-1) - D(i-1,j-1)) / (X(i) - X(i-j+1));
    end
end

% Koeficienti so diagonala
d = diag(D);
end
