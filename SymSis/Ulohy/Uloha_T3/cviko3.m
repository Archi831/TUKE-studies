syms x;
% 1. Vyvorte polynómy:
a = 2*x^3 - 3*x + 1;
b = 3*x^2 + 7*x + 2;
c = x - 3;

% 2. Vyskúšajte operácie násobenia a delenia polynómov:
%  vynásobte polynómy a*b, b*c, a*c
%  vydeľte polynómy a/b

AB = expand(a * b);
BC = expand(b * c);
AC = expand(a * c);
A_B = simplify(a / b);

% 3. Vypočítajte nasledovné derivácie polynómov:
% deriváciu polynómu a
% deriváciu súčinu polynómov b, c
% deriváciu podielu polynómov a, c

dA = diff(a, x);
dAB = diff(BC, x);
dA_B = diff(A_B, x);

% 4. Zistite korene polynómov a, b

rootsA = solve(a, x);
rootsB = solve(b, x);
disp(rootsA);
disp(rootsB);
disp(vpa(root(b)));

% 5. Vypočítajte hodnoty polynómov a, b pre vstupné hodnoty [1 2 3]
inpVals = [1, 2, 3];
valsA = double(subs(a, x, inpVals));
valsB = double(subs(b, x, inpVals));
disp(valsA);
disp(valsB);