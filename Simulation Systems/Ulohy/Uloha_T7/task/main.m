t_span = [0 5];

% PP
x0 = [0; 0]; % y(0)=0, y'(0)=0

[t, x] = ode45(@system_dr, t_span, x0);

plot(t, x(:, 1), 'b-', 'LineWidth', 2, 'DisplayName', 'ode45 y(t)');
hold on;

% analyticke riesenie
y_analyt = (-(1/2) * exp(-2 * t) + (1/3) * exp(-3 * t) + (1/6));
plot(t, y_analyt, 'r--', 'LineWidth', 2, 'DisplayName', 'Analyticke y(t)');

% derivacia
plot(t, x(:, 2), 'g-', 'DisplayName', 'ode45 y''(t)');

% Popisky grafu
title('Riesenie DR y'''' + 5y'' + 6y = 1');
xlabel('Cas t [s]');
ylabel('Amplituda');
legend;
grid on;
hold off;


t_koniec = 5; 

num = [1];
den = [1 5 6];

sys = tf(num, den);
[y_step, t_step] = step(sys, t_koniec);

chyba_riesenia = abs(y_analyt - x(:, 1));
chyba_step = abs(y_step - x(:, 1));

% 2. Vykreslenie chyby do NOVEHO okna
figure; % Otvori nove okno pre graf
plot(t, chyba_riesenia, 'm-', 'LineWidth', 2);
title('Chyba numerickeho riesenia (y_{analyt} - y_{num})');
xlabel('Cas t [s]');
ylabel('Velkost chyby');
grid on;
legend('Chyba y(t)');

figure;
plot(t_step,chyba_step, 'm-', 'LineWidth', 2);
title('Chyba numerickeho riesenia (y_{analyt} - y_{num})');
xlabel('Cas t [s]');
ylabel('Velkost chyby');
grid on;
legend('Chyba y(t)');
