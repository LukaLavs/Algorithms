function v = ZvezniSkalarni(f, g, a, b)
% Funkcija skalarni_produkt izracuna skalarni produkt funkcij f in g 
% kot integral produkta na intervalu [a,b].
%
% Vhod:
%   f, g    funkciji, katerih skalarni produkt racunamo
%   a, b    mejni tocki intervala, na katerem racunamo skalarni produkt
%
% Izhod:
%   v       izracunan skalarni produkt funkcij f in g
%
    v = integral(@(x) f(x) .* g(x), a, b, 'ArrayValued', true);
end