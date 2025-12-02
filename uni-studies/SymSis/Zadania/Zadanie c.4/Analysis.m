function [] = Analysis(sys)
   choice1 = menu("Which domain?", ...
                  "Time domain", "Frequency domain");
   sys_obj = ss(sys.matrices.A, sys.matrices.B, ...
               sys.matrices.C, sys.matrices.D);
switch choice1
case 1
    choice2 = menu("Time domain", ...
        "Step", "Impulse response", "Arbitrary input");
    switch choice2

    case 1
    % Step response
    [y,tout] = step(sys_obj);
    plot(tout, y, 'LineWidth', 3);
    grid on
    title('Step Response of the System');
    xlabel('Time [s]');
    ylabel('Output Response');
    case 2
    % Impulse response
    [y,tout] = impulse(sys_obj);
    plot(tout, y, 'LineWidth', 3);
    grid on
    title('Impulse Response of the System');
    xlabel('Time [s]');
    ylabel('Output Response');
    case 3
    % Arbitrary input
    type = input("Enter signal type (e.g., 'Impulse', 'sinusoid', 'square'): ", 's');
    Ton = input("Enter the duration of the signal (Ton): ");
    Tf = input("Enter the final time (Tf): ");
    Ts = input("Enter the sampling time (Ts): ");
    [u, t] = gensig(type, Ton, Tf, Ts);
    [y_out, t_out, x_out] = lsim(sys_obj, u, t);
    plot(t_out, x_out, 'LineWidth', 1.5); 
    
    grid on;
    title('Dynamics of All 3 Tanks');
    xlabel('Time [s]'); 
    ylabel('Water Level [m]');
    
    % Add legend to identify the tanks
    legend('Tank 1 (Source)', 'Tank 2 (Buffer)', 'Tank 3 (Drain)', 'Location', 'Best');
    end

case 2
    choice3 = menu("Frequency domain", ...
        "Nyquis", "Bode", "Nichols");
    switch choice3
    case 1
        % Nyquist plot
        nyquist(sys_obj);
        title("Nyquist frequency characteristic")
    case 2
        % Bode plot
        bode(sys_obj);
        title("Bode frequency characteristic")
    case 3
        % Nichols plot
        nichols(sys_obj);
        title("Nichols frequency characteristic")
    end
end
end