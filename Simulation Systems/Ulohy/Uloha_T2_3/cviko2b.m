A = [1:3; 6:8; 12:14];
B = [-1:1; -8:-6; 5:7];

sucet = A+B;
rozdiel = A-B;
disp('sucet:');
disp(sucet);
disp('rozdiel:');
disp(rozdiel);

S = [1 2; 3 4];
St = transpose(S);
St2 = St^2;

disp('S transponovana');
disp(St);
disp('St^2:');
disp(St2);

SSt = S*St;
disp('S * St:');
disp(SSt);

S3 = S.*St;
disp('S .* St:');
disp(S3);

S4 = S.^St;
disp('S .^ St:');
disp(S4);