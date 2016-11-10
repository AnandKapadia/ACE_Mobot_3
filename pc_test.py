import cv_toolbox as cv

img = cv.load_image('test1.jpg');
gray = cv.grayscale(img);
gauss = cv.gaussian(gray, 10);
thresh = cv.threshold(gauss, 160, 255);
cv.save_image(gray, 'zgray.jpeg');
cv.save_image(gauss, 'zzgauss.jpeg');
cv.save_image(thresh, 'zzzthresh.jpeg');


