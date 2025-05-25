function [x,X,k] = sekantna(f,x0,x1,tol,N)
    N = N + 1; % tako dobimo res N novih priblizkov
    k = 2;
    fx0 = f(x0);
    fx1 = f(x1);
    x = (x0*fx1 - x1*fx0) / (fx1 - fx0);
    X = [x0; x1; x];
    while abs(x1 - x) > tol && k < N
        k = k + 1;
        x0 = x1;
        fx0 = fx1;
        x1 = x;
        fx1 = f(x);
        x = (x0*fx1 - x1*fx0) / (fx1 - fx0);
        X(end + 1) = x;
    end
end