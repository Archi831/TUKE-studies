function rozdiel = chyba(d, y)
% Funkcia pre výpočet rozdielu a maximálnej chyby
% d = analytické riešenie, y = numerické riešenie
    
    % Vypočíta absolútnu hodnotu rozdielu y_analytickeho a y_numerickeho
    rozdiel = abs(d - y(:, 1));
    
    % Nájdeme maximálnu odchýlku
    chyba = max(rozdiel);
    
    % Vypíšeme výsledok do konzoly
    fprintf('Maximálna odchýlka = %g\n', chyba);
    
    return
end

