% Gauss-Newtonova metoda za e^(polinom n te stopnje)
function [b] = gauss_newton_e(b0, x, y, X, koraki)
    % X = [x.^n, ..., x, ones(size(x), 1)]
    % J = [E po b1, E po b2, ..], kjer E = y_observed - f(b, x)
    % J(br)*[b_{r+1} - b{r}] = - E(br)
    eksponentna = @(b, x) exp(polyval(b, x));
    E = @(b, x) y - exp(polyval(b, x));
    J = @(b, x) - X .* eksponentna(b, x);
    for i=1:koraki
        b = J(b0, x) \ (-E(b0, x) + J(b0, x)*b0);
        b0 = b;
    end
end