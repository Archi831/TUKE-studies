function sys_new = Conversion(sys)
    sys_new = sys;
    choice2 = menu("How would you like to convert?", ...
                   "ss2tf", "tf2ss");
switch choice2
    case 1
        [num,den] = ss2tf(sys.matrices.A, sys.matrices.B, ...
                          sys.matrices.C, sys.matrices.D);
        sys_new.num = num;
        sys_new.den = den;
        disp('Transfer function:');
        disp(['Numerator: ', num2str(sys_new.num)]);
        disp(['Denominator: ', num2str(sys_new.den)]);
    case 2
        if isfield(sys, 'num') && isfield(sys, 'den')
            
        [A, B, C, D] = tf2ss(sys.num, sys.den);
        sys.matrices.A = A;
        sys.matrices.B = B;
        sys.matrices.C = C;
        sys.matrices.D = D;
        disp('State-space representation:');
        disp(['A: ', mat2str(A)]);
        disp(['B: ', mat2str(B)]);
        disp(['C: ', mat2str(C)]);
        disp(['D: ', mat2str(D)]);
        else
            disp('Error: No transfer function defined. Please convert SS to TF first or enter data.');
        end
end
end 