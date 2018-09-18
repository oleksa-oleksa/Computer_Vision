% Gradient Direction
function result = select_gdir(gmag, gdir, mag_min, angle_low, angle_high)
    % TODO Find and return pixels that fall within the desired mag, angle range
    result = gmag >= mag_min & (gdir >= angle_low & gdir <= angle_high);
endfunction

