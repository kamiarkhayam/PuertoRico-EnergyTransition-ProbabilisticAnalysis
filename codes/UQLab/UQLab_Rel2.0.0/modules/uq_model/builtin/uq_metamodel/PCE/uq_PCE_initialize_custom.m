function success = uq_PCE_initialize_custom( current_model, Options)
% success = UQ_PCE_INITIALIZE_CUSTOM(CURRENT_MODEL,OPTIONS) initialize a
%     custom PCE (predictor only) in CURRENT_MODEL based on the options given
%     in the OPTIONS structure
%
% See also: UQ_PCE_INITIALIZE

% initialize return value to 0
success = 0;
if ~isfield(Options, 'PCE')
    error('Custom PCE has been defined, but no PCE field is defined in the options!')
end
customPCE = Options.PCE;

% check that the basis is is defined and retrieve it
if ~isfield(customPCE, 'Basis')
    error('Custom PCE has been defined, but no Basis was specified!')
end
Basis = customPCE.Basis;

% retrieve the basis polynomial indices (\alpha vectors in the documentation)
if ~isfield(Basis, 'Indices')
    error('Custom PCE has been requested, but no basis indices are given!')
end

% retrieve the polynomial types
if ~isfield(Basis, 'PolyTypes')
    error('Custom PCE has been requested, but no polynomial types are given!')
end

% check that the coefficients are available
if ~isfield(customPCE, 'Coefficients')
    error('Custom PCE has been requested, but no polynomial coefficients are given!')
end

% Set the calculation method to 'custom' (no calculation)
current_model.Internal.Method = 'custom';


% Add the missing properties to the current_model object
uq_addprop(current_model, 'PCE');
current_model.PCE =  customPCE;


% Don't allow custom PCE when no input has been defined
if isfield(Options, 'Input') && ~isempty(Options.Input)
    current_model.Internal.Input = uq_getInput(Options.Input);
else
    error('You have not specified an input module! Custom PCE is not allowed when an input module is not specifically defined.');
end

% loop over the output components and check that coefficients and basis
% have the same dimensions. In case the recurrence terms of the orthogonal
% polynomials have not  been calculated, calculate them and add them to the
% Basis structure. 
for oo = 1:length(current_model.PCE)
    if length(current_model.PCE(oo).Coefficients) ~= size(current_model.PCE(oo).Basis.Indices,1)
        error('Custom PCE has been requested, but the number of Coefficients is inconsistent with the number of basis elements for output component %d', oo);
    end
    if ~isfield(current_model.PCE(oo).Basis,'PolyTypesAB')
        [current_model,Options] = uq_PCE_initialize_process_basis(current_model,oo,Options);
        Basis = current_model.PCE.Basis;
    end
end

% add the remaining runtime arguments that may be needed
M = length(current_model.Internal.Input.Marginals);
current_model.Internal.Runtime.M = M;
current_model.Internal.Runtime.nonConstIdx = 1:M;
current_model.Internal.Runtime.MnonConst = M;
current_model.Internal.Runtime.Nout = length(customPCE);
current_model.Internal.Runtime.isCalculated = true;
current_model.Internal.Runtime.current_output = 1;

% add the missing marginals and related parameters
[current_model.Internal.ED_Input.Marginals, ...
    current_model.Internal.ED_Input.Copula] = ...
    uq_poly_marginals(Basis.PolyTypes,...
    Basis.PolyTypesParams);

% set the component-wise properties of the PCE
for oo = 1:length(current_model.PCE)
    nnz_coeff = current_model.PCE(oo).Coefficients ~= 0;
	% maximum degree of active basis
	if sum(nnz_coeff)
		current_model.PCE(oo).Basis.MaxCompDeg = full(max(current_model.PCE(oo).Basis.Indices(nnz_coeff,:),[],1));
	else
		current_model.PCE(oo).Basis.MaxCompDeg = zeros(1, size(current_model.PCE(oo).Basis.Indices,2));
	end
    current_model.PCE(oo).Basis.MaxInteractions = full(max(sum(current_model.PCE(oo).Basis.Indices(nnz_coeff,:) > 0,2)));
    % maximum componentwise degree of candidate basis
    current_model.PCE(oo).Basis.Degree = full(max(max(current_model.PCE(oo).Basis.Indices,[],2)));
    current_model.PCE(oo).Basis.qNorm = 1;
    if sum(nnz_coeff)
        current_model.PCE(oo).Moments.Mean = current_model.PCE(oo).Coefficients(1);
        current_model.PCE(oo).Moments.Var = sum(current_model.PCE(oo).Coefficients(2:end).^2);
    else
        current_model.PCE(oo).Moments.Mean = 0;
        current_model.PCE(oo).Moments.Var = 0;
    end
    
end

% Return, as no further initialization is needed
success = 1;
