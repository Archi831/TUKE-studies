function I = MUN(U, R)
    % Implementacia Metody Uzlovych Napati (MUN) s dvoma superuzlami
    %
    % Neznamne napatia: Vc, Vd, Ve
    % Referencny uzol: Vf = 0V
    % Superuzol 1: Va = Vd + U(1)
    % Superuzol 2: Vb = Ve + U(2)
    
    G = 1 ./ R;
    Is = zeros(3, 1);
    
    % KCL pre Uzol C
    %     pre Superuzol 1 (A, D)
    %     pre Superuzol 2 (B, E)
    M =[(G(2) + G(3) + G(4))  -G(2)                 -G(3);
        -G(2)                 (G(1) + G(2) + G(5))  -G(1);
        -G(3)                 -G(1)                 (G(1) + G(3) + G(6));];

    Is(1) = G(2)*U(1) + G(3)*U(2);
    Is(2) = -(G(1) + G(2))*U(1) + G(1)*U(2);
    Is(3) = G(1)*U(1) - (G(1) + G(3))*U(2);

    % Vyriesime sustavu pre nezname napatia [Vc; Vd; Ve]
    V_nezn = M \ Is;
    
    Vc = V_nezn(1);
    Vd = V_nezn(2);
    Ve = V_nezn(3);
    
    % Vypocitame odvodene napatia
    Va = Vd + U(1);
    Vb = Ve + U(2);
    Vf = 0;
    
    % Vypocitame prudy vo vetvach I(1) az I(6)
    I = zeros(6, 1);
    I(1) = (Vb - Va) / R(1);
    I(2) = (Va - Vc) / R(2);
    I(3) = (Vc - Vb) / R(3);
    I(4) = (Vf - Vc) / R(4);
    I(5) = (Vd - Vf) / R(5);
    I(6) = (Vf - Ve) / R(6);
end
