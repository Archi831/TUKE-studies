function d = analyt(t)
    C1 = 5/8;
    C2 = -5/8;
    C3 = -5/4;
    A  = -5/4;
    
    d = C1.*exp(-t) + C2.*exp(-3*t) + C3.*t.*exp(-3*t) + A.*t.^2.*exp(-3*t);
end