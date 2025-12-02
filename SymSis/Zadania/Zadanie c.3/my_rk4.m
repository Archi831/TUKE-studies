function [t, y] = my_rk4(ndr_fun, tspan, y0, h)
    t = (tspan(1):h:tspan(2))';
    steps = length(t);
    num_vars = length(y0);
    
    y = zeros(steps, num_vars);
    y(1, :) = y0'; 
    
    current_y = y0;
    
    for i = 1:(steps - 1)
        ti = t(i);
        
        k1 = ndr_fun(ti, current_y);
        k2 = ndr_fun(ti + 0.5*h, current_y + 0.5*h*k1);
        k3 = ndr_fun(ti + 0.5*h, current_y + 0.5*h*k2);
        k4 = ndr_fun(ti + h, current_y + h*k3);
        
        current_y = current_y + (h/6) * (k1 + 2*k2 + 2*k3 + k4);
        y(i+1, :) = current_y';
    end
end