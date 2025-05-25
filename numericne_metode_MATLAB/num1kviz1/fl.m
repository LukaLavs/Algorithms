function [FL] = fl(x, b, t, L, U)
    [X, ~, ~] = predstavljiva(b, t, L, U);
    X_leq_x = X(X <= x); 
    X_geq_x = X(X >= x);
    najvecje_manjse_od_x = max(X_leq_x);
    najmanjse_vecje_od_x = min(X_geq_x);
    if abs(najvecje_manjse_od_x - x) <= abs(najmanjse_vecje_od_x - x)
        FL = najvecje_manjse_od_x;
    else
        FL = najmanjse_vecje_od_x;
    end
end