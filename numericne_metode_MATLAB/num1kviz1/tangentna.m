function [x,X,k] = tangentna(f,df,x0,tol,N)
    k = 1;
    x = x0 - f(x0)/df(x0);
    X = [x0; x];
    while abs(x - x0) > tol && k < N
        k = k + 1;
        x0 = x;
        x = x0 - f(x0)/df(x0);
        X(end + 1) = x;
    end
end