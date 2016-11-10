import scipy
import numpy as np
from PIL import Image
from scipy.ndimage.filters import gaussian_filter

#input  string	infilename
#output nparray	data
def load_image(infilename):
    img = Image.open(infilename);
    data = np.array(img);
    return data;

#input nparray npdata
#input string outfilename
#output file saved to system
def save_image(npdata, outfilename):
    img = Image.fromarray(npdata);
    if img.mode != 'RGB':
    	img = img.convert('RGB')
    img.save(outfilename);

#input nparray npdata
#output prints image out to system
def show_image(npdata):
	img = Image.fromarray(npdata);
	img.show();

#input:  np.matrix	img
#output  np.matrix	img_grayscale
def grayscale(rgb):
	r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2];
	gray = 0.2989 * r + 0.5870 * g + 0.1140 * b;
	return gray;

#input:  np.matrix 	img
#input:  int 		k 
#output: np.matrix 	img_gauss
def gaussian(img, sig):
	blurred = gaussian_filter(img, sigma=sig)
	return blurred.astype('uint8');
#input: np.matrix 	img
#input: int 		thresh_val 	(0-255 or -1 for mean of img)
#input: int 		binary_val 	(value for threshold = true)
#output: np.matrix  img_binary	(values 0/binary_val)
def threshold(img, thresh_val, binary_val):
	#calculate threshold value if not given
	if(thresh_val == -1):
		thresh_val = img.mean();
	#return image thresholded
	img_binary = (img > thresh_val) * binary_val;
	return img_binary.astype('uint8');

#input: np.matrix img
#def CV_DoubleRaster(img):


#def CV_Largest_Bin(img, r, c):











