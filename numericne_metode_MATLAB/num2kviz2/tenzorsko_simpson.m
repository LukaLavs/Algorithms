function p = tenzorsko_simpson(f,a,b,c,d,n,m)
% Opis:
%  Približek za integral funkcije f po pravokotniku
%  [a,b]x[c,d] z uporabo tenzorskega Simpsonovega pravila
%
% Vhod
%  f        funkcija, katere integral racunamo (f = @(x,y)...)
%  a,b,c,d  meje integrala
%  n        število notranjih točk v x-smeri
%  m        število notranjih točk v y-smeri
%
% Izhod
%  p        približek za vrednost integrala

    h = (b - a)/(2*n);
    k = (d - c)/(2*m);

    Vx = [1, repmat([4, 2], 1, n - 1), 4, 1];
    Vy = [1, repmat([4, 2], 1, m - 1), 4, 1];
    A = Vx' * Vy;

    X = linspace(a, b, 2*n + 1);
    Y = linspace(c, d, 2*m + 1);

    [X_grid, Y_grid] = ndgrid(X, Y);
    Z = arrayfun(@(x, y) f(x, y), X_grid, Y_grid);
    p = (h*k)/9 * (A(:)' * Z(:));

end

