function [x, y] = vecclenska_eksplicitna(alpha, beta, f, x, y0)
% Eksplicitna veččlenska metoda za ODE sisteme
% y0: m x k matrika začetnih približkov (k korakov)
% x: časovne točke, dolžine N
% alpha, beta: koeficienti metode dolžine k

k = size(y0, 2);  % Število korakov metode
m = size(y0, 1);  % Dimenzija sistema
N = length(x);    % Število točk

y = zeros(m, N);
y(:, 1:k) = y0;

for n = k+1:N
    A = zeros(m, 1);
    B = zeros(m, 1);
    for i = 1:k
        h = x(n-i+1) - x(n-i);  % korak med točkami
        A = A + alpha(i) * y(:, n - i);
        B = B + h * beta(i) * f(x(n - i), y(:, n - i));
    end
    y(:, n) = A + B;
end
y = y';
end
