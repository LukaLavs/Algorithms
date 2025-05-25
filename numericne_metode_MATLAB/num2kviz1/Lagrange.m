function L = Lagrange(f, X, t)
    % f : function handle for values at interpolation points
    % X : vector of interpolation points
    % t : vector of evaluation points
    % L : interpolated values at points t

    Y = f(X);          % Function values at X
    n = length(X);     % Number of interpolation points
    m = length(t);     % Number of evaluation points

    L = zeros(size(t)); % Preallocate output

    for i = 1:n
        Li = ones(size(t)); % Start with ones

        for j = 1:n
            if j ~= i
                Li = Li .* (t - X(j)) / (X(i) - X(j));
            end
        end

        L = L + Y(i) * Li; % Add i-th term
    end
end
