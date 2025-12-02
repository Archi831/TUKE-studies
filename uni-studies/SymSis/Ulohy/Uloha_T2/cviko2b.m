% ulohy 1, 2

A = [1 2 3; 4 5 6; 7 8 9];
disp('matica 3x3: '); disp(A)

a1 = A(1,2);
fprintf('prvok prvého riadku a druhého stĺpca:'); disp(a1);

a2 = A(2,2:3);
fprintf('prvky druhého riadku a druhého až tretieho stĺpca:'); disp(a2);

a3 = A(1,:);
fprintf('prvky prvého riadku:'); disp(a3);

a4 = A(:,3);
disp('prvky tretieho stĺpca:'); disp(a4);

a5 = diag(A);
disp('hlavna diagonála:'); disp(a5);

disp('rozmery matice')
disp(size(A));

a6 = rot90(A);
disp('matica po otočení o 90 stupňov:'); disp(a6);

% uloha 8
v = [10:3:30];
disp('vektor v:'); disp(v);

% uloha 9
ones(3,3)
zeros(2,3)
int16(rand(5,3) * 10)