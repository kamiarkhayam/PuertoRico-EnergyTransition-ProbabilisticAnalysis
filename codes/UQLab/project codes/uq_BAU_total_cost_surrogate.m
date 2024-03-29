function Y = uq_BAU_total_cost_surrogate(X)

X(:,12) = (X(:,12) - 2.5) / 100 + 1; %intensity change adjustment
X(:,13) = (X(:,13) - 65) / 100 + 1; %frequency change adjustment

modelfile = 'C:/Users/bmb2tn/OneDrive - University of Virginia/Ph.D. Projects/Energy PR/codes/surrogates/models/BAU_total_model.json';
weights = 'C:/Users/bmb2tn/OneDrive - University of Virginia/Ph.D. Projects/Energy PR/codes/surrogates/models/BAU_total_model.h5';
net = importKerasNetwork(modelfile,'WeightFile',weights,'OutputLayerType','regression');

Y = predict(net, X);

end