im = imread('bicycle.png');

% BW = edge(I,method) detects edges in image I using the edge-detection algorithm specified by method.

bw = edge(im, 'canny');
imshow(bw)