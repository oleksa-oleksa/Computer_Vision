% Find template 1D
% NOTE: Function definition must be the very first piece of code here!
function index = find_template_1D(t, s)
    % TODO: Locate template t in signal s and return index
    % NOTE: Turn off all output from inside the function before submitting!
    k = 1;
    j = 1;
    while j < length(s)
        if t(k) == s(j)
            k = k + 1;
            j = j + 1;
            if k == lenght(t)
               index = j - k;
            else 
                k = t(k);
                if k < 0
                j = j + 1;
                k = k + 1;
                end
            end
        end   
    end 
    
endfunction