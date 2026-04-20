function sys = Create_hydraulic_model(F1, F2, R1, R2)
    if nargin < 4, R2 = 20000; end
    if nargin < 3, R1 = 20000; end
    if nargin < 2, F2 = 0.20; end
    if nargin < 1, F1 = 0.25; end
    % Fi = Prierezy nadob [m^2]
    % Ri = Hydraulicke odpory [Pa.s/m^3]
    rho = 998;  % Hustota vody [kg/m^3]
    g = 9.81;   % Gravitacia [m/s^2]
    
    % Menovatel je rho * g
    rg = rho * g;
    
    T1 = (F1 * R1) / rg;
    T2 = (F2 * R2) / rg;
    T3 = (F1 * R2) / rg;
    
    % Menovatel pre matice (T1 * T2)
    T1T2 = T1 * T2;
    
    % Matica A (Dynamics)
    % Riadok 2 odpoveda rovnici: q3'' = (1/T1T2)*u - (1/T1T2)*q3 - ((T1+T2+T3)/T1T2)*q3'
    sys.matrices.A = [0, 1; 
                     -1/(T1T2), -(T1 + T2 + T3)/(T1T2)];
                     
    % Matica B (Input)
    sys.matrices.B = [0; 
                      1/(T1T2)];
    
    % Matica C (Output) - Vystupom je prietok q3 (stav x1)
    sys.matrices.C = [1, 0];
    
    % Matica D (Direct feedthrough)
    sys.matrices.D = 0;
    
    % Ulozenie parametrov pre info
    sys.desc = 'M5.5: Hydraulicky system - dve nadoby';
    sys.T = [T1, T2, T3];
    
    disp('Model Hydraulickeho systemu nacitany.');
    disp(['Parametre: F1=', num2str(F1), ' m2, F2=', num2str(F2), ' m2']);
    disp(['Odpory: R1=R2=', num2str(R1)]);
end