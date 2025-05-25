function y = euler_eks(x, f, y0)
% Funkcija izračuna približke za vrednosti 
% rešitve začetnega problema z
% eksplicitno Eulerjevo metodo
%
% Vhod
%  x = [x0, ... , xn]: delilne točke
%  f funkcija:  y'(x) = f(x, y(x))
%  y0: začetni pogoj
%
% Izhod
%  y = [y0, .., yn]: približki
n = length(x);
m = length(y0);
y = zeros(m, n);
y(:, 1) = y0;
for i=1:n-1
    h = x(i+1) - x(i);
    y(:, i+1) = y(:, i) + h * f(x(i), y(:, i));
end
y = y';
end

