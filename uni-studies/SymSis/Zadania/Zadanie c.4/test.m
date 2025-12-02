% GenerovanieGrafov_Zadanie4.m
% Skript pre simulaciu 3 scenarov (Rampa, Skok, Pulzy)
% pre model 3 hydraulickych nadob (Zadanie 4)

clc; clear; close all;

% 1. Nacitanie modelu (s defaultnymi parametrami)
sys_struct = Create_hydraulic1_model();
% Prevod na LTI objekt (State-Space)
sys_obj = ss(sys_struct.matrices.A, sys_struct.matrices.B, ...
             sys_struct.matrices.C, sys_struct.matrices.D);

% 2. Nastavenie casu a pociatocnych podmienok
T_sim = 2000;          % Celkovy cas simulacie [s]
dt = 1;                % Krok simulacie
t = 0:dt:T_sim;        % Casovy vektor

% Pociatocne podmienky (hladiny v case 0 nie su nulove, podla obrazka)
x0 = [0.2; 0.25; 0.1]; % [h1; h2; h3] v metroch

% 3. Definicia vstupnych signalov q_in(t)

% SCENAR A: Rampa (Linearny narast a ustalenie)
% Narast z 0 na 0.003 medzi t=0 a t=300, potom konstanta
u_ramp = zeros(size(t));
max_flow = 0.01; % 3e-3 m3/s
t_ramp_end = 300;
for i = 1:length(t)
    if t(i) <= t_ramp_end
        u_ramp(i) = (max_flow / t_ramp_end) * t(i);
    else
        u_ramp(i) = max_flow;
    end
end

% SCENAR B: Skok (Konstantny pritok od zaciatku)
u_step = ones(size(t)) * max_flow;

% SCENAR C: Pulzy (Rampa a potom vypadky)
u_pulse = u_ramp; % Zacneme rampou
% Pridame "diery" (nulovy pritok) v urcitych intervaloch
pulse_width = 100;
gaps = [800, 1100, 1400, 1700]; % Zaciatky vypadkov
for g = gaps
    idx_start = find(t >= g, 1);
    idx_end = find(t >= g + pulse_width, 1);
    u_pulse(idx_start:idx_end) = 0;
end


% 4. Simulacia (lsim)
% lsim vracia: y (vystup), t (cas), x (vsetky stavy h1, h2, h3)
[y_ramp, t, x_ramp] = lsim(sys_obj, u_ramp, t, x0);
[y_step, t, x_step] = lsim(sys_obj, u_step, t, x0);
[y_pulse, t, x_pulse] = lsim(sys_obj, u_pulse, t, x0);


% 5. Vykreslenie (Layout 3x2 podla vzoru)
figure('Name', 'Simulacia modelov', 'Color', 'w', 'Position', [100, 100, 1000, 800]);

% --- Riadok 1: RAMPA ---
subplot(3,2,1);
plot(t, u_ramp, 'b', 'LineWidth', 1.5);
title('Vstupný prítok (Rampa)');
ylabel('q_{in} [m^3/s]'); grid on;
ylim([0, max_flow*1.2]);

subplot(3,2,2);
plot(t, x_ramp(:,1), 'r', 'LineWidth', 1.2); hold on;
plot(t, x_ramp(:,2), 'g', 'LineWidth', 1.2);
plot(t, x_ramp(:,3), 'b', 'LineWidth', 1.5);
title('Hladiny v nádobách (Rampa)');
legend('h_1', 'h_2', 'h_3 (výstup)');
ylabel('h [m]'); grid on;

% --- Riadok 2: SKOK ---
subplot(3,2,3);
plot(t, u_step, 'b', 'LineWidth', 1.5);
title('Vstupný prítok (Skok)');
ylabel('q_{in} [m^3/s]'); grid on;
ylim([0, max_flow*1.2]);

subplot(3,2,4);
plot(t, x_step(:,1), 'r', 'LineWidth', 1.2); hold on;
plot(t, x_step(:,2), 'g', 'LineWidth', 1.2);
plot(t, x_step(:,3), 'b', 'LineWidth', 1.5);
title('Hladiny v nádobách (Skok)');
ylabel('h [m]'); grid on;

% --- Riadok 3: PULZY ---
subplot(3,2,5);
plot(t, u_pulse, 'b', 'LineWidth', 1.5);
title('Vstupný prítok (Pulzy)');
xlabel('čas [s]'); ylabel('q_{in} [m^3/s]'); grid on;
ylim([0, max_flow*1.2]);

subplot(3,2,6);
plot(t, x_pulse(:,1), 'r', 'LineWidth', 1.2); hold on;
plot(t, x_pulse(:,2), 'g', 'LineWidth', 1.2);
plot(t, x_pulse(:,3), 'b', 'LineWidth', 1.5);
title('Hladiny v nádobách (Pulzy)');
xlabel('čas [s]'); ylabel('h [m]'); grid on;