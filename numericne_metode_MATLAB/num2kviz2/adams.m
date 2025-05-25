function y = adams(x, f, y0, y1, y2)
% Funkcija izračuna približke za vrednosti 
% rešitve začetnega problema z
% eksplicitno Eulerjevo metodo
%
% Vhod
%  x = [x0, ... , xn]: delilne točke
%  f funkcija:  y'(x) = f(x, y(x))
%  y0,y1,y2: začetni približki
%
% Izhod
%  y = [y0, .., yn]: približki

y0 = [y0, y1, y2];
alpha = [1, 0, 0];
beta = [23/12, -4/3, 5/12];
[~, y] = vecclenska_eksplicitna(alpha, beta, f, x, y0);
    
end