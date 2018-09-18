close all
clear
home

%% Edge Filter in Matlab
im = imread('bicycle.png');

% BW = edge(I,method) detects edges in image I using the edge-detection algorithm specified by method.

bw = edge(im, 'canny');
imshow(bw)

%% Lena 

% Read and convert to grayscale
lena = imread('lena.png');
lena = rgb2gray(lena);

figure, imshow(lena), title ('Original image monochrome');

% Make smoothed/blured image
h = fspecial('gaussian', [11 11], 4);

figure, surf(h), title ('Filter Graph');

lenaSmooth = imfilter(lena, h);
figure, imshow(lenaSmooth), title ('Smoothed image monochrome');

%% Method 1: Shift left and right and show diff image
lenaL = lenaSmooth;
lenaR = lenaSmooth;

% shifting
lenaL(:, 1:(end - 1)) = lenaL(:, 2:end); 
lenaR(:, 2:end) = lenaR(:, 1:(end - 1));

lenaDiff = double(lenaR) - double(lenaL);

% Pass a second argument as an empty vector to deal with negative numbers
% we could get after biulding the difference image
figure, imshow(lenaDiff, []), title ('Difference between right and left shifted images');

%% Method 2: Canny edge detector
lenaCanny = edge(lena, 'canny');
figure, imshow(lenaCanny), title ('Original Canny edges');

lenaSmoothCanny = edge(lenaSmooth, 'canny');
figure, imshow(lenaSmoothCanny), title ('Original Canny smooth edges');

%% Method 3: Laplacian of Gaussian

lenaLog = edge(lena, 'log');
figure, imshow(lenaLog), title ('Laplacian of Gaussian');
