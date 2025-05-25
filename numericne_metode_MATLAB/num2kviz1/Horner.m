function v = Horner(X, d, t)
    % Funkcija horner izračuna vrednost interpolacijskega polinoma p (zapisanega v Newtonovi obliki) v točkah t.
    %
    % Vhod:
    %   X    seznam interpolacijskih točk (X = [x_0, x_1, ..., x_n])
    %   d    koeficienti polinoma (d = [d_0, d_1, ..., d_n], ki so deljene diference)
    %   t    točke, v katerih računamo vrednost polinoma p
    %
    % Izhod:
    %   v    vrednosti polinoma p v točkah iz seznama t

    % Inicializacija vektorja vrednosti
    v = d(end) * ones(size(t));  % Set initial value to the last coefficient

    % Iterira skozi koeficiente v nasprotnem vrstnem redu
    for i = (length(X)-1):-1:1
        v = d(i) + (t - X(i)) .* v; 
    end
end