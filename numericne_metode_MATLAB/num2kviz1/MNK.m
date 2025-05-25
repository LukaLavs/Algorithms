function [koef, gram, desna] = MNK(F, baza, a, b, skalarni, N)
% Funkcija MNK izračuna aproksimant za funkcijo F po metodi 
% najmanjših kvadratov (MNK) v dani bazi za zvezni skalarni produkt na 
% intervalu [a,b].
%
% Vhod:
%   F       funkcija, ki jo aproksimiramo
%   baza    celica baznih funkcij
%   a, b    mejni točki intervala, na katerem aproksimiramo funkcijo F
%
% Izhod:
%   koef    vektor koeficientov, ki določajo linearno kombinacijo funkcij 
%           iz baze za aproksimacijo funkcije F
%   gram    Gramova matrika, ki vsebuje skalarne produkte baznih funkcij
%   desna   vektor desne strani, ki vsebuje skalarne produkte
%           funkcije F z baznimi funkcijami

n = length(baza);  % Število baznih funkcij

% Izračun Gramove matrike
gram = zeros(n, n);
for i = 1:n
    for j = 1:n
        if (skalarni == "Diskretni")
            gram(i, j) = DiskretniSkalarni(baza{i}, baza{j}, a, b, N);
        elseif (skalarni == "Zvezni") 
            gram(i, j) = ZvezniSkalarni(baza{i}, baza{j}, a, b);
        end
    end
end

% Izračun desne strani
desna = zeros(n, 1);
for i = 1:n
    if (skalarni == "Diskretni")
        desna(i) = DiskretniSkalarni(F, baza{i}, a, b, N);
    elseif (skalarni == "Zvezni")
        desna(i) = ZvezniSkalarni(F, baza{i}, a, b);
    end
end

% Rešitev sistema linearnih enačb
koef = gram \ desna;
end