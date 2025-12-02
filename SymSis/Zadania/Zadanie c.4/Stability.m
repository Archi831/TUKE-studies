function []=Stability(sys)

p = eig(sys.matrices.A);
s = size(p);
is_stable = 1;

for i = 1:s(:,1)

    if real(p(i)) > 0
        disp("Not stable")
        is_stable = 0;
        break
    end
end

if is_stable == 1
    disp("The system is marginaly stable")
end

end