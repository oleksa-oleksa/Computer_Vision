close all
clear
home

% Udacity 2A-L1 Images as functions
% Introduction to computer vison, methods for application and machine
% learning classification

dolphin = imread('dolphin.png'); % load image

%==================================
% Different ways to plot the image

figure
imshow(dolphin)

line([1 512], [256 256], 'color', 'r')

%==================================

disp(size(dolphin))
disp(class(dolphin))

%==================================
% Image values at a given location (row, col)
dolphin(50, 100)

figure
plot(dolphin(50, :))

% TODO: Extract a 2D slice between rows 101 to 103 and columns 201 to 203 (inclusive)
dolphin(101:103, 201:203)


% Crop an image
bicycle = imread('bicycle.png');
figure
imshow(bicycle);

disp(size(bicycle));  % check size

cropped = bicycle(110:310, 10:160);
figure
imshow(cropped);

% TODO: Find out cropped image size
disp(size(cropped))


% Color planes
fruit = imread('fruit.png');
figure
imshow(fruit);

disp(size(fruit));

% TODO: Select a color plane, display it, inspect values from a row
fruits_blue = fruit(:,:,3);
figure
imshow(fruits_blue)

% Add two images
summed = dolphin + bicycle;
figure
imshow(summed);

average = 0.5 * dolphin + 0.5 * bicycle; % better preserves pixels values
figure
imshow(average);

figure
imshow(scale(dolphin, 1.5));

figure
imshow(blend(dolphin, bicycle, 0.75));