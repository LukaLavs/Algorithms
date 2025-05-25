function S = GeneralizedBernstein(f, n, t)
    % f : function handle
    % n : degree of the approximation
    % t : evaluation point(s), scalar or vector
    % S : approximated value(s) using generalized Bernstein

    S = zeros(size(t));     % initialize result
    denom = zeros(size(t)); % denominator of the weights

    for j = 0:n
        denom = denom + nchoosek(n, j) .* t.^j .* (1 - t).^(n - j);
    end

    for i = 0:n
        numer = nchoosek(n, i) .* t.^i .* (1 - t).^(n - i);
        w = numer ./ denom;
        S = S + f(i / n) .* w;
    end
end

%f = @(x) sqrt(x);
%n = 10;
%t = linspace(0, 1, 1000);
%S = GeneralizedBernstein(f, n, t);

%plot(t, f(t), 'k--', t, S, 'r-');
%legend('Original f(x)', 'Generalized Bernstein');
%grid on;
