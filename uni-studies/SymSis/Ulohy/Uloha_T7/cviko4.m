    %Pomocou funkcie ode23 riešte diferenciálne rovnice:
% y'' + 2y' + 2y = 0, y(0) = 1, y'(0) = 1
% y'' - 4y' + 3y = 2, y(0) = 1, y'(0) = -3

% Skript na riešenie D.R. y'' + 2y' + 2y = 0

clear; clc; close all;

% 1. Definovanie funkcie pre systém D.R. 1. rádu
% Vstup 't' je čas, 'y' je stavový vektor [y(1); y(2)]
% y(1) zodpovedá Y_1 (čiže y)
% y(2) zodpovedá Y_2 (čiže y')
%
% Naša sústava:
% y(1)' = y(2)
% y(2)' = -2*y(1) - 2*y(2)
dydt = @(t, y) [y(2); -6*y(1) - 5*y(2)];

% 2. Definovanie časového intervalu
% Riešime napríklad od t=0 do t=10
tspan = [0 10];

% 3. Definovanie počiatočných podmienok
% y(0) = 1  => y(1) na začiatku je 1
% y'(0) = 1 => y(2) na začiatku je 1
y0 = [1; 1];

% 4. Riešenie sústavy pomocou ode23
% 't' bude vektor časových bodov
% 'Y' bude matica, kde prvý stĺpec Y(:,1) je naše hľadané y(t)
% a druhý stĺpec Y(:,2) je jeho derivácia y'(t)
[t, Y] = ode45(dydt, tspan, y0);

% 5. Vykreslenie výsledku (riešenie y(t))
figure;
subplot(211); plot(t, Y(:, 1), 'b-o', 'LineWidth', 1.5);
title("Riešenie D.R.: y'' + 2y' + 2y = 0");
xlabel('Čas (t)');
ylabel('y(t)');
legend('y(t)');
subplot(212); plot(t, Y(:, 2), 'r-o', 'LineWidth', 1.5);
title("Riešenie D.R.: y'' + 2y' + 2y = 0");
xlabel('Čas (t)');
ylabel('y(t)');
legend('y(t)');
plot(t,Y);

grid on;