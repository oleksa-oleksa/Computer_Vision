close all
clear
home

hsize = 32;
sigma = 4;

% h = fspecial('gaussian',hsize,sigma) returns a rotationally symmetric 
% Gaussian lowpass filter of size hsize with standard deviation sigma. 
% Not recommended. Use imgaussfilt or imgaussfilt3 instead.
h = fspecial('gaussian', hsize, sigma);

% Surface plot
figure
surf(h);

% imagesc(C) displays the data in array C as an image 
% that uses the full range of colors in the colormap. 
figure
imagesc(h);

%============================================
im = imread('dolphin.png'); % load image

for sigma = 1:5:26
    h = fspecial('gaussian', hsize, sigma);
    % B = imfilter(A,h) filters the multidimensional array A 
    % with the multidimensional filter h and returns the result in B.
    outim = imfilter(im, h);
    figure;
    imshow(outim);
end

%============================

% B = imgaussfilt(A,sigma) filters image A with a 2-D Gaussian smoothing kernel 
% with standard deviation specified by sigma.
outim = imgaussfilt(im, sigma);
figure
imshow(outim);




