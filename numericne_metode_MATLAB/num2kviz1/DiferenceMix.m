function coeffs = DeljeneDiferenceMix(x_values, y_values)
    % This function calculates the coefficients for Newton's interpolation polynomial.
    % x_values: the x points
    % y_values: the corresponding y values
    % Output: coeffs, the coefficients of the Newton interpolation polynomial
    
    % Sort the x and y values
    [x_values, idx] = sort(x_values);
    y_values = y_values(idx);

    % Initialize the coefficients array
    n = length(x_values);
    coeffs = zeros(n, 1);
    
    % Calculate the Newton coefficients
    for i = 1:n
        coeffs(i) = deljena_diferenca(x_values(1:i), x_values, y_values);
    end
end

function val = deljena_diferenca(D, x_values, y_values)
    % This recursive function calculates the divided differences
    k = length(D);  % The length of the subset D
    
    if k == 1
        % Base case: return the corresponding y value
        val = y_values(find(x_values == D(1), 1));
    elseif all(D == D(1))
        % If all x values in D are the same, compute the derivative
        val = k_th_derivate(D(1), k-1, x_values, y_values) / factorial(k-1);
    else
        % Recursive case: calculate the divided differences
        val = (deljena_diferenca(D(2:end), x_values, y_values) - ...
               deljena_diferenca(D(1:end-1), x_values, y_values)) / (D(end) - D(1));
    end
end

function val = k_th_derivate(x, k, x_values, y_values)
    % This function finds the k-th derivative of y_values at x
    index = find(x_values == x, 1) + k;
    val = y_values(index);
end







% Example usage of the NewtonInterpolation function

% Define some example points
x_values = [0, 1/4, 15/13, 3];    % x values
f = @(x) cos(5./(x+1));           % Function
df = @(x) 5 ./ (x + 1).^2 .* sin(5 ./ (x + 1));  % Derivative

% Calculate the function and derivative values at the points
y_values = f(x_values);
dY_values = df(x_values);

% Combine x values and y values (function and derivative)
X1 = [x_values, x_values];  % Combine x values for function and derivatives
Y1 = [y_values, dY_values]; % Combine corresponding y values

% Calculate the coefficients for the Newton interpolation polynomial
coeffs = DeljeneDiferenceMix(X1, Y1);

% Display the results
disp('Newton interpolation coefficients:');
disp(coeffs);
