function [x, y_vals] = Butcher_eksplicit(butcher, f, x, y0)
% alpha  : c-vektor (časovni premiki v Butcherjevi shemi)
% gamma  : b-vektor (uteži)
% A      : matrika koeficientov (Butcherjeva shema)
% f      : funkcija f(x, y)
% x      : vektor delilnih točk [x0, x1, ..., xn]
% y0     : začetni pogoj (vektor)

alpha = butcher(1:end-1, 1);
gamma = butcher(end, 2:end);
BETA = butcher(1:end-1, 2:end);

s = length(gamma);        % število stopenj metode
N = length(x);            % število točk
n = length(y0);           % dimenzija sistema

y_vals = zeros(N, n);     % rešitve
y_vals(1, :) = y0(:)';    % začetna vrednost

for i = 1:N-1
    h = x(i+1) - x(i);
    xi = x(i);
    yi = y_vals(i, :)';

    k = zeros(n, s);
    for j = 1:s
        y_stage = yi;
        for l = 1:j-1
            y_stage = y_stage + h * BETA(j,l) * k(:,l);
        end
        t_stage = xi + alpha(j) * h;
        k(:,j) = f(t_stage, y_stage);
    end

    y_next = yi;
    for j = 1:s
        y_next = y_next + h * gamma(j) * k(:,j);
    end

    y_vals(i+1, :) = y_next';
end

end