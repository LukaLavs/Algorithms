function [v] = DiskretniSkalarni(f, g, a, b, N)
% Funkcija DiskretniSkalarni izračuna diskretni skalarni produkt 
% funkcij f in g na intervalu [a,b] z N+1 enakomerno izbranimi točkami.
%
% Vhod:
%   f, g      funkciji, katerih diskretni skalarni produkt računamo
%   a, b      mejni točki intervala, na katerem računamo diskretni 
%             skalarni produkt
%   N+1       število enakomerno razporejenih točk na intervalu [a,b]
%
% Izhod:
%   v         vrednost diskretnega skalarnega produkta funkcij f in g
%
    X = linspace(a, b, N + 1);
    v = (b-a)/(N+1) * sum(f(X) .* g(X));
end