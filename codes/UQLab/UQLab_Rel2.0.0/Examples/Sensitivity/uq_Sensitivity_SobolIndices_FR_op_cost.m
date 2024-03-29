%% SENSITIVITY: MC
%
% In this example, Sobol' sensitivity indices for the 
% <https://uqworld.org/t/borehole-function/ borehole function>
% are calculated with three different methods:
% Monte Carlo (MC) simulation, polynomial chaos expansion (PCE), 
% and canonical low-rank approximation (LRA).

%% 1 - INITIALIZE UQLAB
%
% Clear variables from the workspace,
% set random number generator for reproducible results,
% and initialize the UQLab framework:
clearvars
results = [];
resultsFirst = [];
for i = 1:1000
    rng(i,'twister')
    uqlab
    disp(i);
    
    %% 2 - COMPUTATIONAL MODEL
    %
    % The computational model is an $8$-dimensional analytical formula 
    % that is used to model the water flow through a borehole.
    % The borehole function |uq_borehole| is supplied with UQLab.
    %
    % Create a MODEL object from the function file:
    ModelOpts.mFile = 'uq_FR_op_cost_Surrogate.m';
    
    myModel = uq_createModel(ModelOpts);
    
    %%
    % Type |help uq_borehole| for information on the model structure as well as
    % the description of each variable.
    
    %% 3 - PROBABILISTIC INPUT MODEL
    %
    % The probabilistic input model consists of eight independent random 
    % variables.
    %
    % Specify the marginals as follows:
    InputOpts.Marginals(1).Name = 'bioPricePercentile';
    InputOpts.Marginals(1).Type = 'Uniform';
    InputOpts.Marginals(1).Parameters = [0 1]; 
    
    %InputOpts.Marginals(2).Name = 'urnPricePercentile';
    %InputOpts.Marginals(2).Type = 'Uniform';
    %InputOpts.Marginals(2).Parameters = [0 1]; 
    
    InputOpts.Marginals(2).Name = 'battPercentileFix';
    InputOpts.Marginals(2).Type = 'Uniform';
    InputOpts.Marginals(2).Parameters = [0 1]; 
    
    InputOpts.Marginals(3).Name = 'hydPercentileFix';
    InputOpts.Marginals(3).Type = 'Uniform';
    InputOpts.Marginals(3).Parameters = [0 1]; 
    
    InputOpts.Marginals(4).Name = 'solPercentileFix';
    InputOpts.Marginals(4).Type = 'Uniform';
    InputOpts.Marginals(4).Parameters = [0 1]; 
    
    InputOpts.Marginals(5).Name = 'windPercentileFix';
    InputOpts.Marginals(5).Type = 'Uniform';
    InputOpts.Marginals(5).Parameters = [0 1]; 

    InputOpts.Marginals(6).Name = 'popPercentile';
    InputOpts.Marginals(6).Type = 'Uniform';
    InputOpts.Marginals(6).Parameters = [0 1]; 

    InputOpts.Marginals(7).Name = 'perCapitaPercentile';
    InputOpts.Marginals(7).Type = 'Uniform';
    InputOpts.Marginals(7).Parameters = [0 1]; 

    InputOpts.Marginals(8).Name = 'corruptionFactor'; 
    InputOpts.Marginals(8).Type = 'Uniform';
    InputOpts.Marginals(8).Parameters = [1 4];
    
    %%
    % Create an INPUT object based on the specified marginals:
    myInput = uq_createInput(InputOpts);
    
    %% 4 - SENSITIVITY ANALYSIS
    %
    % Sobol' indices are calculated first with a direct MC simulation 
    % of the model and subsequently through post-processing of the
    % coefficients of its PCE and LRA approximation.
    
    %% 4.1 MC-based Sobol' indices
    %
    % Select the sensitivity analysis module in UQLab
    % and the Sobol' analysis method:
    SobolOpts.Type = 'Sensitivity';
    SobolOpts.Method = 'Sobol';
    
    %%
    % Specify the maximum order of the Sobol' indices to be calculated:
    SobolOpts.Sobol.Order = 3;
    
    %%
    % Specify the sample size for the MC simulation:
    SobolOpts.Sobol.SampleSize = 5e4;
    %%
    % Note that the total cost of computation is $(M+2) \times N$,
    % where $M$ is the input dimension and $N$ is the sample size.
    % Therefore, the total cost for the current setup is
    % $(8+2) \times 10^5 = 10^6$ evaluations of the full computational model.
    
    %%
    % Run the sensitivity analysis:
    mySobolAnalysisMC = uq_createAnalysis(SobolOpts);
    
    %%
    % Retrieve the analysis results for comparison:
    mySobolResultsMC = mySobolAnalysisMC.Results;
    
    results_total(:, i) = mySobolResultsMC.Total;
    results_first(:, i) = mySobolResultsMC.FirstOrder;


end