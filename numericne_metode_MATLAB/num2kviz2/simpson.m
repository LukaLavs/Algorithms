function p = simpson(f, a, b, m)
% Opis:
%  Približek za integral funkcije f na intervalu [a,b]
%  z uporabo sestavljenega Simpsonovega pravila.
%
% Vhod
%  f        funkcija, katere integral racunamo (f = @(x)...)
%  a,b      krajisci intervala
%  m        število podintervalov za sestavljeno pravilo.
%
% Izhod
%  p        približek za vrednost integrala

    X = linspace(a, b, 2*m + 1);
    V = [1, repmat([4, 2], 1, m - 1), 4, 1];
    h = (b-a)/(2*m);
    p = h/3 * f(X) * V';
end
