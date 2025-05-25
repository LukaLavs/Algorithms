function Bf = Bernpoly(f, n, x)
    % Funkcija bernpoly vrne vrednosti Bernsteinovega polinoma stopnje n za funkcijo f v
    % tockah x.
    % 
    % Bf = bernpoly(f, n, x)
    % 
    % Vhod:
    %  f    funkcija: @(x) f(x),
    %  n    stopnja Bernsteinovega polinoma,
    %  x    seznam abscis.
    % 
    % Izhod:
    %  Bf   seznam vrednosti Bernsteinovega polinoma stopnje n za funkcijo f v
    %       tockah iz seznama x.
    
    % Initialize the output vector for Bernstein polynomial values
    Bf = zeros(size(x));  % Same size as input x
    
    % Loop over each value of x to calculate the Bernstein polynomial at that point
    for i = 1:length(x)
        xi = x(i);  % Current value of x
        
        % Compute the Bernstein polynomial at xi
        sum_val = 0;
        for k = 0:n
            % Binomial coefficient: n choose k
            binom = nchoosek(n, k);
            
            % Evaluate the function f at the point k/n
            f_val = f(k / n);
            
            % Compute the Bernstein basis function and accumulate
            sum_val = sum_val + binom * f_val * (1 - xi)^(n-k) * xi^k;
        end
        
        % Store the computed value in the output vector
        Bf(i) = sum_val;
    end
end