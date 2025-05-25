function [y] = Lyb(L, b)
    n = size(L, 2);
    y = zeros(n, 1);
    for i = 1:n
        S = 0;
        for k = 1:(i-1)
            S = S + L(i, k)*y(k);
        end
        y(i) = b(i) - S;
    end
end