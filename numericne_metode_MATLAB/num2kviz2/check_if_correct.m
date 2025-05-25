function check_if_correct(x, Y, f, y0)
% x    : časovni vektor
% Y    : vaša rešitev (m x N matrika, m komponent, N časovnih točk)
% f    : funkcija f(t, y)
% y0   : začetni pogoj (m x 1 ali 1 x m)

% Reši z ode45 za referenco
[t_ref, y_ref] = ode45(f, x, y0);

% Pretvori vašo rešitev v enako obliko kot ode45 (tudi transponira)
%Y = Y';         % Pretvori v N x m
n_comp = size(Y, 2);  % Število komponent

% Plot
figure;
for i = 1:n_comp
    subplot(n_comp, 1, i);
    plot(x, Y(:, i), 'b', 'LineWidth', 1.5); hold on;
    plot(t_ref, y_ref(:, i), 'r--', 'LineWidth', 1.2);
    title(['Component y_', num2str(i)]);
    xlabel('t'); ylabel(['y_', num2str(i)]);
    legend('Custom method', 'MATLAB ode45');
    grid on;
end
end
