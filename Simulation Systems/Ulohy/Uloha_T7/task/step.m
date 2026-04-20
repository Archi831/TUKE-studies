
t_koniec = 5; 

num = [1];
den = [1 5 6];

sys = tf(num, den);
[y_step, t_step] = step(sys, t_koniec);

figure; 
plot(t_step, y_step, 'r-', 'LineWidth', 2);

title('G(s) = 1 / (s^2 + 5s + 6)');
xlabel('Cas t [s]');
ylabel('Amplituda');
legend('step');
grid on;

sys