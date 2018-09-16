% Find template 2D
% NOTE: Function definition must be the very first piece of code here!
function [yIndex xIndex] = find_template_2D(template, img)
    % TODO: Find template in img and return [y x] location
    % NOTE: Turn off all output from inside the function before submitting!
    c = normxcorr2(template, img);
    [yIndex, xIndex] = find(c == max(c(:))); 
    
    yIndex = yIndex - size(template, 1) + 1;
    xIndex = xIndex - size(template, 2) + 1;
end

