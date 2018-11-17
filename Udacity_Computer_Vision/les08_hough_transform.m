close all
clear
home

img = imread('shapes.png');
grays = rgb2gray(img);
edges = edge(grays, 'canny');

figure, imshow(img), title('Original image');
figure, imshow(grays), title('Grayscale image');
figure, imshow(edges), title('Edge pixels');

% Apply hough transform to find candidate lines
[accum, theta, rho] = hough(edges);
figure, imagesc(accum, 'XData', theta, 'YData', rho), title('Hough accumulator');

% Find peaks in the Hough accumulator matrix

% original peaks
% peaks = houghpeaks(accum, 100);

% increased peaks
peaks = houghpeaks(accum, 100, 'Threshold', ceil(0.6 * max(accum(:))), 'NHoodSize', [5, 5]);

hold on; 
plot(theta(peaks(:, 2)), rho(peaks(:, 1)), 'rs');
hold off;
size(peaks)

% Find lines (segments) in the image
%line_seg = houghlines(edges, theta, rho, peaks)

line_seg = houghlines(edges, theta, rho, peaks, 'FillGap', 50, 'MinLength', 100)


figure, imshow(img), title('Line segments');
hold on;
for k = 1:length(line_seg)
    endpoints = [line_seg(k).point1; line_seg(k).point2];
    plot(endpoints(:, 1), endpoints(:, 2), 'LineWidth', 2, 'Color', 'green');
end
hold off;
