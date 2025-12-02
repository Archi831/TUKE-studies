function passed = Skuska(I)
    if abs(I(2)) + abs(I(3)) - abs(I(4)) <1e-6
        if abs(I(4)) - abs(I(5)) - abs(I(6)) <1e-6
            passed = true;
        else
            passed = false;
        end
    else
        passed = false;
    end
end 