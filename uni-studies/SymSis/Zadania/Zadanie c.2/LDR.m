function xder = LDR(t, x)
% Zápis diferenciálnej rovnice 3. rádu pomocou 3 rovníc 1. rádu
    
    % x(1) = y, x(2) = y', x(3) = y''
    xder = [
        x(2);                                % x1' = x2
        x(3);                                % x2' = x3
        -7*x(3)-15*x(2)-9*x(1) + 5*exp(-3*t) % x3' = -7x3 - 15x2 - 9x1 + 5e^-3t
    ];
end



