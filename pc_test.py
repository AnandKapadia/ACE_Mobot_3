import cv_toolbox as cv
import numpy as np
import time

img = cv.load_image('test1.jpg');
img = cv.subsample_image(img, 20, 20);
gray = cv.grayscale(img);
gauss = cv.gaussian(gray, 3);
thresh = cv.threshold(gauss, 150, 255);
debug = 0;
if debug:
	(img_avg, angle) = cv.angle(thresh, debug);
else:
	angle = cv.angle(thresh, debug);

cv.save_image(gray, 'zgray.jpeg');
cv.save_image(gauss, 'zzgauss.jpeg');
cv.save_image(thresh, 'zzzthresh.jpeg'); 
if(debug):
	(row, col) = img_avg.shape;
	for r in range(0, row):
		for c in range(0, col):
			img_avg[r][int(col/2 + (angle * (r-row)))] = 255;
	cv.save_image(img_avg, 'zzzzangle.jpeg');

