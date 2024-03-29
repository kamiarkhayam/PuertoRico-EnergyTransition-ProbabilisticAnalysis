function uq_postProcessInversion(module, varargin)
% UQ_POSTPROCESSINVERSION post-processes an inverse analysis carried out
%    with the Bayesian inversion module.
%
% See also: UQ_POSTPROCESSINVERSIONMCMC, UQ_POSTPROCESSINVERSIONSSLE

%% CONSISTENCY CHECKS
if ~strcmp(module.Type, 'uq_inversion')
    error('uq_postProcessInversionMCMC only operates on objects of type ''Inversion''') 
end

% check which Solver and call solver-specific post-processer.
currSolver = module.Internal.Solver.Type;
if strcmp(currSolver, 'MCMC')
    uq_postProcessInversionMCMC(module, varargin{:})
elseif strcmp(currSolver, 'SLE')
    uq_postProcessInversionSLE(module, varargin{:})
elseif strcmp(currSolver, 'SSLE')
    uq_postProcessInversionSSLE(module, varargin{:})
else
    error('Nothing to post-process for solver %s!',currSolver)
end

end