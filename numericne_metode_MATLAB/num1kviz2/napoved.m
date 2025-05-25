% Napovedovanje vrednosti portfolija naslednjo uro z polinomom stopnje n:
function [result] = napoved(A, ura)
    result = 0;
    for j = 1:size(A, 2)
        koef = polyfit([0, 1, 2], [A(10, j), A(11, j), A(12, j)], n);
        result = result + polyval(koef, ura);
    end
end