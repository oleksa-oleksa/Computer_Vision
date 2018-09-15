close all
clear
home

im = imread('peppers.jpg');

hsize = 32;
sigma = 8;
h = fspecial('gaussian', hsize, sigma);

% clip filter 
imout = imfilter(im, h, 0);
figure;
imshow(imout);

% clip filter 
imout = imfilter(im, h, 256);
figure;
imshow(imout);

% wrap around
imout = imfilter(im, h, 'circular');
figure;
imshow(imout);

% copy edge (good)
imout = imfilter(im, h, 'replicate');
figure;
imshow(imout);

% reflect accros edge (pretty well)
imout = imfilter(im, h, 'symmetric');
figure;
imshow(imout);
