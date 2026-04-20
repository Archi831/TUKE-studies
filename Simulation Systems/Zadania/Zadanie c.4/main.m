sys = Create_hydraulic1_model();
while true
choice = menu('Main Menu', 'Input Parameters', 'Conversion', 'Analysis', 'Stability', 'Exit');

switch choice
    case 1 % Input Parameters
        sys = Input(sys);
    case 2 % Conversion
        sys = Conversion(sys);
    case 3 % Analysis
        Analysis(sys)
    case 4 % Stability
        Stability(sys)
    case 5 % Exit
        disp('Exiting...');
        break;
end
end