function sys = Create_model(m,k,b)
    if nargin < 3, b = 1; end % damping
    if nargin < 2, k = 2;  end % stiffness
    if nargin < 1, m = 50;  end % mass

    sys.matrices.A = [0 1; -k/m -b/m];
    sys.matrices.B = [0; 1/m];
    sys.matrices.C = [1 0];
    sys.matrices.D = 0;
end