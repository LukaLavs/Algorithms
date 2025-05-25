function y = euler_mod(x, f, y0)
% Funkcija izračuna približke za vrednosti 
% rešitve začetnega problema z
% modificirano Eulerjevo metodo
%
% Vhod
%  x = [x0, ... , xn]: delilne točke
%  f funkcija:  y'(x) = f(x, y(x))
%  y0: začetni pogoj
%
% Izhod
%  y = [y0, .., yn]: približki
butcher = [0, 0, 0;
           0.5, 0.5, 0;
           inf, 0, 1];
[~, y] = Butcher_eksplicit(butcher, f, x, y0);
end