close all
clear
home


% Test code 1D:
s = [-1 0 0 1 1 1 0 -1 -1 0 1 0 0 -1];
t = [1 1 0];
disp('Signal:'), disp([1:size(s, 2); s]);
disp('Template:'), disp([1:size(t, 2); t]);

index = find_template_1D(t, s);
disp('Index:'), disp(index);

disp('=================')
disp('Test code 2D:')

% Test code 2D:
tablet = imread('dolphin.png');
figure
imshow(tablet);
glyph = tablet(75:165, 150:185);
figure
imshow(glyph);

[y x] = find_template_2D(glyph, tablet);
disp([y x]); % should be the top-left corner of template in tablet