function F = uq_triangular_cdf( X, parameters )
% UQ_TRIANGULAR_CDF(X, parameters) calculates the Cumulative Density Function
% values of samples X  that follow a triangular distribution with parameters 
% specified in the vector 'parameters'

a = parameters(1);
b = parameters(2);
c = parameters(3);

F = zeros(size(X));

%% set the CDF to 0 below the lower bound
idx = X <= a;
F(idx) = 0;

%% set the CDF to the appropriate value in the valid range
idx = X > a & X < c ;
F(idx) = (X(idx) - a).^2 /(b-a)/(c-a);
idx = X > c & X < b ;
F(idx) = 1 - (b - X(idx)).^2 /(b-a)/(b-c);

%% set the CDF to 1 above the bound 
idx = X >= b ;
F(idx) = 1;
