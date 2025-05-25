function P = WFunction(X, t)
    % t : scalar or vector of evaluation points
    % x : vector of roots (x1, x2, ..., xn)
    % P : value(s) of (t - x1)(t - x2)...(t - xn)

    % Use broadcasting to subtract each x from t, then take product
    T = t(:);           % column vector for broadcasting
    X = X(:)';          % row vector
    diffs = T - X; % matrix of (t_i - x_j)
    P = prod(diffs, 2); % product along each row
end
