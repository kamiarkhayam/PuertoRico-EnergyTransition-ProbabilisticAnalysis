function Y = uq_BAU_op_cost_surrogate(X)

modelfile = 'C:/Users/bmb2tn/OneDrive - University of Virginia/Ph.D. Projects/Energy PR/codes/surrogates/models/BAU_op_model.json';
weights = 'C:/Users/bmb2tn/OneDrive - University of Virginia/Ph.D. Projects/Energy PR/codes/surrogates/models/BAU_op_model.h5';
net = importKerasNetwork(modelfile,'WeightFile',weights,'OutputLayerType','regression');

Y = predict(net, X);

end