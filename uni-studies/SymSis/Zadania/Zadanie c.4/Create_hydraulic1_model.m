function sys = Create_hydraulic1_model(F1, F2, F3, R12, R23, Rout)
    if nargin < 6, Rout = 50; end
    if nargin < 5, R23 = 50; end
    if nargin < 4, R12 = 50; end
    if nargin < 3, F3 = 3.0; end
    if nargin < 2, F2 = 1.5; end
    if nargin < 1, F1 = 1.5; end
    % Physical Constants
    % F1, F2, F3: Cross-sectional areas of the tanks
    % R12, R23, Rout: Hydraulic resistances
    
    % Matrix A
    a11 = -1/(F1*R12);
    a12 =  1/(F1*R12);
    
    a21 = 1/(F2*R12);
    a22 =  -(1/(F2*R12) + 1/(F2*R23));
    
    a32 =  1/(F3*R23);
    a33 = -1/(F3*Rout);
    
    sys.matrices.A = [a11, a12, 0;
                      a21, a22, 0;
                      0  , a32, a33];

    % Matrix B
    sys.matrices.B = [1/F1; 
                         0; 
                         0];
                     
    % Matrix C
    sys.matrices.C = [0, 0, 1];
    
    % Matrix D
    sys.matrices.D = 0;
end