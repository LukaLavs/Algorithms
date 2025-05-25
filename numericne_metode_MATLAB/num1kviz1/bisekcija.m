function [x,X] = bisekcija(f,a,b,N)
    X = zeros(N, 1);
    for i = 1:N
        c = (a + b) / 2;
        X(i) = c;
        if (sign(f(a)) ~= sign(f(c)))
            b = c;
        else
            a = c;
        end
    end
    x = X(end);
end