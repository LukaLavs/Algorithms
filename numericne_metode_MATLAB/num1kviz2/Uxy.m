function [x] = Uxy(U, y)
    % Elementi na diag(U) neničelni
    n = size(U, 2);
    x = zeros(n, 1);
    for i = n:-1:1 % start step end
        S = 0;
        for k = (i+1):n
            S = S + U(i, k)*x(k);
        end
        x(i) = (1/U(i, i)) * (y(i) - S);
    end
end