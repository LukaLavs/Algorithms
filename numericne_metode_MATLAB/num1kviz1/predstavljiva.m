function [X, Xn, Xd] = predstavljiva(b, t, L, U)
    M = zeros(b^t,1);
    i = 1;
    for c1 = 0:b-1
        for c2 = 0:b-1
            for c3 = 0:b-1
                for c4 = 0:b-1
                    %ci, i=t je max i torej U !!!!!!
                    m = c1*b^-1 + c2*b^-2 + c3*b^-3 + c4*b^-4;
                    M(i) = m;
                    i = i+1;
                end
            end
        end
    end

    d = U-L+1;
    bm = b^(t-1);
    Xpn = zeros((b-1)*bm,d);
    for j = 1:d
        e = L+j-1;
        Xpn(:,j) = M(bm+1:end)*b^e;
    end
    Xpn = Xpn(:);
    Xn = [-Xpn(end:-1:1); Xpn];

    % denormalizirana stevila
    Xpd = M(2:bm)*b^L;
    Xd = [-Xpd(end:-1:1); Xpd];
    
    % predstavljiva stevila (brez 0, Inf, -Inf, NaN)
    X = [Xn(1:end/2); Xd(1:end/2); Xpd; Xpn];
end