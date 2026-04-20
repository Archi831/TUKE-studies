% Využitím funkcie polyder a roots nájdite extrém funkcie y(t) t^2-2t+6
syms t;
y = t^2 - 2*t + 6;
dy = polyder([1 -2 6])
extrema = roots(dy)

% Nájdite rozklad na parciálne zlomky nasledujúcich funkcií

syms x;

f = (x^5)/(x^4-x^2);
g = 36/(x^5 - 2*x^4 - 2*x^3 + 4*x^2 + x - 2);

partF = partfrac(f)
partG = partfrac(g)

h = 1/(x^3+3*x^2+2*x);
partH = partfrac(h)

disp(partH)