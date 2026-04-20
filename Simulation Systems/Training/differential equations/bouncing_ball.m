
tspan = [0 10];
x0 = [10; 0];

options = odeset("Events", @eventf, "Refine", 10);
[t, x] = ode45(@f, tspan, x0, options);

x1 = x; 
t1 = t;
for i = 1:9
[t,x] = ode45(@f, [t1(end), 100], [0, -x1(end)*0.9], options);
x1 = [x1; x];
t1 = [t1; t];
end

comet(t1,x1(:,1))

function xder = f(~,x)
g=9.8;
xder = [x(2); -g];
end

function [check, terminal, direction] = eventf(~, x)
check = x(1);
terminal = 1;
direction = -1;
end