function sys_new = Input(sys)
   
choice = menu("How would you like to define your system", ...
              "In polynomials", "With Zeros, Poles and Gain", ...
              "With matices", "With physical parameters");
switch choice
    case 1
        disp('--- Hybrid 3-Tank Hydraulic System Setup ---');
        disp('Configure rational function for the linear model.');
        sys.num = input("Enter the numerator=");
        sys.den = input("Enter the denominator=");

    case 2
        disp('--- Hybrid 3-Tank Hydraulic System Setup ---');
        disp('Configure zpk for the linear model.');
        z = input("Enter zeros.. z=");
        p = input("Enter poles.. p=");
        k = input("Enter gain.. k=");
        [sys.num, sys.den] = zp2tf(z,p,k);
        
    case 3
        disp('--- Hybrid 3-Tank Hydraulic System Setup ---');
        disp('Configure matices for the linear model.');
        sys.matices.A = input("Enter matrix A=");
        sys.matices.B = input("Enter matrix B=");
        sys.matices.C = input("Enter matrix C=");
        sys.matices.D = input("Enter matrix D=");

    case 4
        disp('--- Hybrid 3-Tank Hydraulic System Setup ---');
        disp('Configure physical parameters for the linear model.');
        
        % 1. Geometry Inputs
        r1 = input('Enter Radius of Tank 1 [m] (default 0.4): ');
        if isempty(r1), r1 = 0.4; end
        
        r2 = input('Enter Radius of Tank 2 [m] (default 0.4): ');
        if isempty(r2), r2 = 0.4; end
        
        r3 = input('Enter Radius of Tank 3 [m] (default 0.5): ');
        if isempty(r3), r3 = 0.5; end
        
        % Convert Radii to Cross-Sectional Areas (F = pi * r^2)
        F1 = pi * r1^2;
        F2 = pi * r2^2;
        F3 = pi * r3^2;
        
        % 2. Flow Resistance Inputs
        disp('--- Hydraulic Resistances ---');
        disp('(Higher value = Thinner pipe/Harder to flow)');
        
        R12 = input('Resistance T1 <-> T2 (default 5): ');
        if isempty(R12), R12 = 5; end
        
        R23 = input('Resistance T2 -> T3 (default 5): ');
        if isempty(R23), R23 = 5; end
        
        Rout = input('Resistance Drain T3 (default 5): ');
        if isempty(Rout), Rout = 5; end
        
        % 3. Create Model
        sys = Create_hydraulic_model(F1, F2, F3, R12, R23, Rout);
        
        disp('System created successfully!');
        disp(['Areas calculated: F1=', num2str(F1,3), ' F2=', num2str(F2,3), ' F3=', num2str(F3,3)]);
end
sys_new = sys;
end