function dxdt = system_dr(~, x)
    u = 1;

    dxdt = zeros(2,1);
    
    % x1' = x2
    dxdt(1) = x(2);
    
    % x2' = -6*x1 - 5*x2 + u
    dxdt(2) = -6*x(1) - 5*x(2) + u;
end