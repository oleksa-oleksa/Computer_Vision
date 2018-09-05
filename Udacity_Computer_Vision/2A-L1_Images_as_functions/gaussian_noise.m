close all
clear
home

some_number = randn();

noise1 = randn([1 1000]);
noise2 = randn([1 1000]);


[n1, x1] = hist(noise1, linspace(-3, 3, 21));
[n2, x2] = hist(noise2, linspace(-3, 3, 21));

figure
subplot(1, 2, 1)
plot(x1, n1)
subplot(1, 2, 2)
plot(x2, n2)


% TODO: Try generating other kinds of random numbers.
%       How about a 2D grid of random Gaussian values?

figure
noise3 = randn([3 1000]);

dolphin = imread('dolphin.png'); % load image
% multiplying a bunch of random numbers generated from a Gaussian or Normal 
% distribution changes their effective standard deviation, 
% i.e. how far apart the values are spread.
sigma = 1;
% Generates the noise the same size as an image
% No layers mixing, dolphin image determines the size of a noise image only
noisy_pic = randn(size(dolphin)).*sigma;
imshow(noisy_pic)

% this will add a noise to an image
output = noisy_pic + doplhin
