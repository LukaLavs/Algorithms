% Gauss-Newton splošna:  (ni preverjena)
% Imejmo sistem f1(x1, x2, ...) = 0; f2(x1, ...) = 0; ...
% Označimo F(x) vektor [f1;, ...,; fn]
% Izračunajmo J(x) kot [df1/dx1, ..., df1/dxn; df2/dx1, ...]
% izračunamo xn+1 = xn - J(xn)^-1 * F(xn)
% kot parameter vstavi @J, @F, ...
function [b] = gauss_newton(b0, x, y, J, F, koraki)
    for i=1:koraki
        b = J(b0, x) \ (-E(b0, x) + J(b0, x)*b0);
        b0 = b;
    end
end