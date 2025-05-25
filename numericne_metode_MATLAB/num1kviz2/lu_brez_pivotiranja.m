function [L, U] = lu_brez_pivotiranja(A)
    n = size(A, 2);
    for k = 1:(n-1)
        for i = (k+1):n
            A(i, k) = A(i, k) / A(k, k);
            for j = (k+1):n
                A(i, j) = A(i, j) - A(i, k) .* A(k, j);
            end
        end
    end
    U = triu(A);
    L = eye(n) + tril(A, -1);
end