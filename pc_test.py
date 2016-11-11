import cv_toolbox as cv
import numpy as np

img = cv.load_image('test1.jpg');
gray = cv.grayscale(img);
gauss = cv.gaussian(gray, 10);
thresh = cv.threshold(gauss, 160, 255);
(img_avg, angle) = cv.angle(thresh, 0);

#cv.save_image(gray, 'zgray.jpeg');
#cv.save_image(gauss, 'zzgauss.jpeg');
#cv.save_image(thresh, 'zzzthresh.jpeg'); 
#(row, col) = img_avg.shape;
#for r in range(0, row):
#	for c in range(0, col):
#		img_avg[r][int(col/2 + (angle * (r-row)))] = 255;
#cv.save_image(img_avg, 'zzzzangle.jpeg');

