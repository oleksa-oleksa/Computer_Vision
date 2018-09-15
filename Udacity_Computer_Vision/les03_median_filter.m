close all
clear
home

im = imread('moon.png');

% Add noise to image
noisy_im = imnoise(im, 'salt & pepper', 0.02);
figure;
imshow(noisy_im);

% J = medfilt2(I) performs median filtering of the image I 
% in two dimensions. Each output pixel contains the median value 
% in a 3-by-3 neighborhood around the corresponding pixel in the input image.
median_filtered = medfilt2(noisy_im);
figure;
imshow(median_filtered);