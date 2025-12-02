function dxdt = ndr_system(t, x)
    % y'' + y' + y^2 = 2*exp(-t)
    % x(1) = y
    % x(2) = y'
    
    dxdt = zeros(2, 1);
    dxdt(1) = x(2);
    dxdt(2) = 2*exp(-t) - x(2) - x(1)^2;
end