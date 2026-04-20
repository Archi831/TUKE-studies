% 1. Definovanie počiatočných podmienok a rozsahu
t_start = 0; 
t_end = 5;
tspan = [t_start t_end]; 

% Počiatočné podmienky: y(0)=1, y'(0)=0, y''(0)=0
Y0 = [0; 0; 0]; 

% 2. Numerické riešenie pomocou ODE45
% 'difrov' je názov súboru s definíciou DR (systém 1. rádu)
[t, y] = ode45(@LDR, tspan, Y0); 
% y(:,1) obsahuje numerické riešenie y(t)
yn = y(:, 1);

% 3. Analytické riešenie
ya = analyt(t); 

% 4. Výpočet chyby
rozdiel = chyba(ya, y);

% 5. Grafické porovnanie
figure(1);

subplot(2, 1, 1);
plot(t, yn, 'b-');
title('Numerické riešenie y(t)');
xlabel('t');
ylabel('y_n(t)');
grid on;

subplot(2, 1, 2);
plot(t, ya, 'g--');
title('Analytické riešenie y(t)');
xlabel('t');
ylabel('y_a(t)');
grid on;

% Pre lepšie porovnanie (obe riešenia v jednom grafe)
figure(2);
plot(t, yn, 'b-', 'LineWidth', 2); hold on;
plot(t, ya, 'g--', 'LineWidth', 1); hold off;
title('Porovnanie numerického a analytického riešenia');
legend('Numerické (y_n)', 'Analytické (y_a)', 'Location', 'NorthWest');
xlabel('t');
ylabel('y(t)');
grid on;

% 6. Zobrazenie chyby
figure(3);
plot(t, rozdiel, 'r-', 'LineWidth', 1.5);
title('Chyba medzi numerickým a analytickým riešením');
xlabel('t');
ylabel('Chyba');
grid on;