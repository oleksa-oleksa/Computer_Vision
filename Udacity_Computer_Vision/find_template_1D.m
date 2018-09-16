% Find template 1D
% NOTE: Function definition must be the very first piece of code here!
function index = find_template_1D(t, s)
    % TODO: Locate template t in signal s and return index
    % NOTE: Turn off all output from inside the function before submitting!
    
    % C = normxcorr2(template,A) computes the normalized cross-correlation of the matrices template and A. 
    % The resulting matrix C contains the correlation coefficients.
   c = normxcorr2(t, s);
   [maxValue rawIndex] = max(c)
   index = rawIndex - size(t, 2) + 1
end