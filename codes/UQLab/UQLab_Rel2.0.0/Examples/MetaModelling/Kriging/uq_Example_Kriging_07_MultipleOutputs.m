%% KRIGING METAMODELING: MULTIPLE OUTPUTS
%
% This example showcases an application of Kriging to the metamodeling
% of a simply supported beam model with multiple outputs.
% The model computes the deflections at several points along the length 
% of the beam subjected to a uniform random load.

%% 1 - INITIALIZE UQLAB
%
% Clear all variables from the workspace, set the random number generator
% for reproducible results, and initialize the UQLab framework:
clearvars
rng(50,'twister')
uqlab

%% 2 - COMPUTATIONAL MODEL
%
% The simply supported beam problem is shown in the following figure:
uq_figure
[I,~] = imread('SimplySupportedBeam.png');
image(I)
axis equal
set(gca, 'visible', 'off');

%% 
% The (negative) deflection of the beam at any longitudinal coordinate
% $s$ is given by:
%
% $$V(s) = -\frac{p \,s (L^3 - 2\, s^2 L + s^3) }{2E b h^3}$$
%
% This computation is carried out by the function
% |uq_SimplySupportedBeam9Points(X)| supplied with UQLab.
% The function evaluates the inputs gathered in the $N \times M$
% matrix |X|, where $N$ and $M$ are the numbers of realizations
% and inputs, respectively.
% The inputs are given in the following order:
%
% # $b$: beam width $(m)$
% # $h$: beam height $(m)$
% # $L$: beam length $(m)$
% # $E$: Young's modulus $(Pa)$
% # $p$: uniform load $(N/m)$
%
% The function returns the beam deflection $V(s_i)$
% at nine equally-spaced points along the length
% $s_i = i \cdot L/10, \; i=1,\ldots,9.$ 
%
% Create a MODEL object from the |uq_SimplySupportedBeam9points| function:
ModelOpts.mFile = 'uq_SimplySupportedBeam9points';

myModel = uq_createModel(ModelOpts);

%% 3 - PROBABILISTIC INPUT MODEL
%
% The simply supported beam model has five independent input parameters
% modeled by lognormal random variables.
% The parameters of the distributions are given in the following table:

%%
% <html>
% <table border=1><tr>
% <td><b>Variable</b></td>
% <td><b>Description</b></td>
% <td><b>Distribution</b></td>
% <td><b>Mean</b></td>
% <td><b>Std. deviation</b></td></tr>
% <tr>
% <td>b</td>
% <td>Beam width</td>
% <td>Lognormal</td>
% <td>0.15 m</td>
% <td>7.5 mm</td>
% </tr>
% <tr>
% <td>h</td>
% <td>Beam height</td>
% <td>Lognormal</td>
% <td>0.3 m</td>
% <td>15 mm</td>
% </tr>
% <tr>
% <td>L</td>
% <td>Length</td>
% <td>Lognormal</td>
% <td>5 m</td>
% <td>50 mm</td>
% </tr>
% <tr>
% <td>E</td>
% <td>Young modulus</td>
% <td>Lognormal</td>
% <td>30000 MPa</td>
% <td>4500 MPa</td>
% </tr>
% <tr>
% <td>p</td>
% <td>Uniform load</td>
% <td>Lognormal</td>
% <td>10 kN/m</td>
% <td>2 kN/m</td>
% </tr>
% </table>
% </html>

%%
% Define an INPUT object with the following marginals:
InputOpts.Marginals(1).Name = 'b'; % beam width
InputOpts.Marginals(1).Type = 'Lognormal';
InputOpts.Marginals(1).Moments = [0.15 0.0075]; % (m)

InputOpts.Marginals(2).Name = 'h'; % beam height
InputOpts.Marginals(2).Type = 'Lognormal';
InputOpts.Marginals(2).Moments = [0.3 0.015]; % (m)

InputOpts.Marginals(3).Name = 'L'; % beam length
InputOpts.Marginals(3).Type = 'Lognormal';
InputOpts.Marginals(3).Moments = [5 0.05]; % (m)

InputOpts.Marginals(4).Name = 'E'; % Young's modulus
InputOpts.Marginals(4).Type = 'Lognormal';
InputOpts.Marginals(4).Moments = [3e10 4.5e9] ; % (Pa)

InputOpts.Marginals(5).Name = 'p'; % uniform load
InputOpts.Marginals(5).Type = 'Lognormal';
InputOpts.Marginals(5).Moments = [1e4 2e3]; % (N/m)

%%
% Create an INPUT object based on the marginals:
myInput = uq_createInput(InputOpts);

%% 4 - KRIGING METAMODEL
%
% Select the Kriging metamodeling tool:
MetaOpts.Type = 'Metamodel';
MetaOpts.MetaType = 'Kriging';

%%
% Assign the previously created INPUT and MODEL objects
% to the metamodel options:
MetaOpts.Input = myInput;
MetaOpts.FullModel = myModel;
%%
% If an INPUT object and a MODEL object are specified,
% an experimental design is automatically generated
% and the corresponding model responses are computed.

%%
% Specify the sampling strategy and the number of sample points
% for the experimental design:
MetaOpts.ExpDesign.Sampling = 'LHS';
MetaOpts.ExpDesign.NSamples = 150;

%%
% Set a linear trend:
MetaOpts.Trend.Type = 'linear';

%%
% Use the exponential correlation family:
MetaOpts.Corr.Family = 'exponential';

%%
% Use maximum-likelihood-based hyperparameter estimation:
MetaOpts.EstimMethod = 'ML';

%%
% Use the hybrid genetic algorithm (GA)-based to solve the hyperparameters
% estimation problem:
MetaOpts.Optim.Method = 'HGA';

%%
% Set the maximum number of generations and the population size:
MetaOpts.Optim.MaxIter = 50;
MetaOpts.Optim.HGA.nPop = 50;

%%
% Reduce the verbosity during optimization:
MetaOpts.Optim.Display = 'none';

%%
% Create the Kriging metamodel:
myKriging = uq_createModel(MetaOpts);

%% 5 - VALIDATION
%
% The deflections $V(s_i)$ at the nine points are plotted
% for three realizations of the random inputs.
% Relative length units are used for comparison,
% because $L$ is one of the random inputs.

%% 5.1 Create and evaluate a validation sample
%
% Generate a validation sample:
Nval = 3;
Xval = uq_getSample(Nval);

%%
% Evaluate the full computational model at the validation sample:
Yval = uq_evalModel(myModel,Xval);

%%
% Evaluate the Kriging metamodel at the same sample points:
YKRG = uq_evalModel(myKriging,Xval);

%% 5.2 Visualize results
%
% For each sample points of the validation set $\mathbf{x}^{(i)}$,
% the simply supported beam deflection $\mathcal{M}(\mathbf{x}^{(i)})$
% is compared against the one predicted by the Kriging metamodel
% $\mathcal{M}^{KRG}(\mathbf{x}^{(i)})$ (its mean):
li = 0:0.1:1;  % use normalized positions (length-wise)

uq_figure
% Plot each realization with a different color
cmap = uq_colorOrder(Nval);
for ii = 1:Nval
    uq_plot(...
        li, [0,Yval(ii,:),0], '-',...
        li, [0,YKRG(ii,:),0], ':x',...
        'Color', cmap(ii,:));
    hold on
end
hold off

uq_legend(...
    {'$\mathrm{\mathcal{M}(\mathbf{x}^{(1)})}$',...
        '$\mathrm{\mathcal{M}^{KRG}(\mathbf{x}^{(1)})}$',...
        '$\mathrm{\mathcal{M}(\mathbf{x}^{(2)})}$',...
        '$\mathrm{\mathcal{M}^{KRG}(\mathbf{x}^{(2)})}$',...
        '$\mathrm{\mathcal{M}(\mathbf{x}^{(3)})}$',...
        '$\mathrm{\mathcal{M}^{KRG}(\mathbf{x}^{(3)})}$'},...
    'Location', 'north')

xlabel('$\mathrm{L_{rel}}$ (-)')
ylabel('$\mathrm{V}$ (m)')
