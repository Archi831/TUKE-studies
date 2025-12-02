% zadanie 2
e=[2,4,1,12,0,5];
f=[0,8,6,3,10,7];
fprintf('e: '); disp(e);
fprintf('f: '); disp(f);

l_xor = xor(e,f);
fprintf('logicky XOR: '); disp(l_xor);

l_and = and(e,f);
fprintf('logicky AND: '); disp(l_and);

l_or = or(e,f);
fprintf('logicky OR: '); disp(l_or);

r_bigger = e>f;
fprintf('e > f: '); disp(r_bigger);
r_smaller = e<f;
fprintf('e < f: '); disp(r_smaller);

% zadanie 3
f_selection = f(f<10 & f>5);
fprintf('Selected elements from f (5 < f < 10): '); disp(f_selection);

% zadanie 4
z1 = 5i;
z2 = 3 + 4*pi*1i;
z3 = (2/3)*pi*1i;

fprintf('Komplexne cislo 5i: '); disp(z1);
fprintf('Komplexne cislo 3 + 4pi.i: '); disp(z2);
fprintf('Komplexne cislo 2/3pi.i: '); disp(z3);

z1/0
z2/0
z3/0