% Program na vypocet prudov vo vetvach obvodu podla prilozenj schemy.
% Vypocet sa uskutocnuje metodou sluckovych prudov
% na zaklade uzivatelom zadanych hodot napat. zdrojov a odporov.

% Vstupne hodnoty
U = input('Zadaj hodonoty nap. zdrojov vo voltoch v tvare "[U1 U2]"\n');
R = input('Zadaj hodnoty odporov v Omoch v tvare "[R1 R2 R3 R4 R5 R6]"\n');

% [20 40]
% [6 3 2 1 5 4]
% --- Vypocet pomocou MSP ---
I_msp = MSP(U, R);

% --- Vypocet pomocou MUN ---
I_mun = MUN(U, R);

if Skuska(I_msp)
    disp(" ")
    disp("MSP prudy vo vetvach vychovuju 1.KZ")
else
    disp("MSP prudy vo vetvach nevychovuju 1.KZ");
end
if Skuska(I_mun)
    disp("MUN prudy vo vetvach vychovuju 1.KZ");
else 
    disp("MUN prudy vo vetvach nevychovuju 1.KZ");
end

% Vypis prudov a porovnanie
fprintf('\nPorovnanie prudov vo vetvach (I1..I6) [MSP vs MUN]:\n\n');
fprintf('         MSP        |        MUN\n');
fprintf('--------------------------------------\n');
fprintf('I(1) = %10.6f A | %10.6f A\n', I_msp(1), I_mun(1));
fprintf('I(2) = %10.6f A | %10.6f A\n', I_msp(2), I_mun(2));
fprintf('I(3) = %10.6f A | %10.6f A\n', I_msp(3), I_mun(3));
fprintf('I(4) = %10.6f A | %10.6f A\n', I_msp(4), I_mun(4));
fprintf('I(5) = %10.6f A | %10.6f A\n', I_msp(5), I_mun(5));
fprintf('I(6) = %10.6f A | %10.6f A\n', I_msp(6), I_mun(6));


