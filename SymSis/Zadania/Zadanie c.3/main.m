clear; clc; close all;

t_span = [0, 10];
y0 = [0; 1];     % y(0)=0, y'(0)=1
h = 0.05;        % for RK4

[t_rk, y_rk] = my_rk4(@ndr_system, t_span, y0, h);

options = odeset('RelTol', 1e-6, 'AbsTol', 1e-6);
[t_ode, y_ode] = ode45(@ndr_system, t_span, y0, options);

subplot(2,1,1);
plot(t_ode, y_ode(:,1), 'b-', 'LineWidth', 2); 
hold on;
plot(t_rk, y_rk(:,1), 'r--', 'LineWidth', 1.5);
title('Riesenie y(t) - Porovnanie');
xlabel('Cas [s]'); ylabel('Amplituda y(t)');
legend('ODE45', 'Custom RK4', 'Location', 'best');
grid on;

subplot(2,1,2);
plot(y_ode(:,1), y_ode(:,2), 'b-', 'LineWidth', 1.5); 
hold on;
plot(y_rk(:,1), y_rk(:,2), 'r--', 'LineWidth', 1.5);
title('Trajektória fázovej roviny (y vs y'')');
xlabel('y(t)'); ylabel('y''(t)');
grid on;

y_ode_interp = interp1(t_ode, y_ode(:,1), t_rk, 'spline');
max_error = max(abs(y_rk(:,1) - y_ode_interp));
fprintf('Maximálna odchýlka = %.6f\n', max_error);





