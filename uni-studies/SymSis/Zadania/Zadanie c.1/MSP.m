function I = MSP(U, R)
    % Implementacia Metody sluckovych prudov (MSP)

    A = [R(1)+R(2)+R(3), -R(2),           -R(3);
        -R(2),            R(2)+R(4)+R(5), -R(4);
        -R(3),           -R(4),            R(3)+R(4)+R(6)];
    B = [0; -U(1); U(2)];

    % Vyriesime sustavu pre nezname prudy [Is1; Is2; Is3]
    Is = A\B;

    % Vypocitame prudy vo vetvach I(1) az I(6)
    I = zeros(6, 1);
    I(1) = Is(1);
    I(2) = Is(1) - Is(2);
    I(3) = Is(1) - Is(3);
    I(4) = Is(2) - Is(3);
    I(5) = Is(2);
    I(6) = Is(3);
return