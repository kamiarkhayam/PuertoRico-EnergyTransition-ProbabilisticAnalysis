function Y = uq_FR_op_cost_surrogate(X)

modelfile = 'C:/Users/bmb2tn/OneDrive - University of Virginia/Ph.D. Projects/Energy PR/codes/surrogates/models/FR_op_model.json';
weights = 'C:/Users/bmb2tn/OneDrive - University of Virginia/Ph.D. Projects/Energy PR/codes/surrogates/models/FT_op_model.h5';
net = importKerasNetwork(modelfile,'WeightFile',weights,'OutputLayerType','regression');


% populationPercentile = X(:, 6);
% xi = 2.68236383e+03;
% omega = 1.38613090e+02;
% alpha = 4.56670101e-01;
% % Using norminv function, which is MATLAB's equivalent to Python's stats.norm.ppf
% population = skewnorm_inv_cdf(populationPercentile, xi, omega, alpha) * 1000;
% 
% perCapitaPercentile = X(:, 7);
% xi = 1.20194609e+00;
% omega = 7.97378754e-02;
% alpha = 4.56670101e-01;
%    
% 
% % Assuming 'percentile' is provided or defined elsewhere in your MATLAB code
% coef = skewnorm_inv_cdf(perCapitaPercentile, xi, omega, alpha);
% 
% perCapita = 5602 * coef;
% 
% 
% demand = population .* perCapita / (277.78 * 10^6);
% coef = 277777.778;
% 
% 
% Y = predict(net, X) .* demand / coef;

Y = predict(net, X);

end