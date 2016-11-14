import scipy
import numpy as np
from PIL import Image
from scipy.ndimage.filters import gaussian_filter
from scipy import stats

#input  string	infilename
#output nparray	data
def load_image(infilename):
    img = Image.open(infilename);
    data = np.array(img);
    return data;

def subsample_image(img, subset_row, subset_col):
	return img[::subset_row, ::subset_col];

#input nparray npdata
#input string outfilename
#output file saved to system
def save_image(npdata, outfilename):
	npdata = npdata.astype('uint8');
	img = Image.fromarray(npdata);
	if img.mode != 'RGB':
		img = img.convert('RGB');
	img.save(outfilename);

#input nparray npdata
#output prints image out to system
def show_image(npdata):
	npdata = npdata.astype('uint8');
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
	return blurred

#input: np.matrix 	img
#input: int 		thresh_val 	(0-255 or -1 for mean of img)
#input: int 		binary_val 	(value for threshold = true)
#output: np.matrix  img_binary	(values 0/binary_val)
def threshold(img, thresh_val, binary_val):
	#return image thresholded
	img_binary = (img > thresh_val) * binary_val;
	return img_binary;



#this function is SUPER SLOW
#input: np.matrix img, rastsers on 0 vs val
#inputL int 	  val
def double_raster(img, val):
	#get size
	(row, col) = img.shape;
	#initalize raster
	raster = img;
	#initialize first value of first bin
	index = 2;

	#initial runthrough, assign bins
	for r in range(0,row):
		for c in range(0, col):
			#if the current pixel should be binned
			if(raster[r][c] == val):
				#if pixel to left has a bin, set to same
				if(r != 0 and raster[r-1][c] != 0):
					raster[r][c] = raster[r-1][c];
				#if pixel to up has a bin, set to same
				elif(c != 0 and raster[r][c-1] != 0):
					raster[r][c] = raster[r][c-1];
				#otherwise create new bin
				else:
					raster[r][c] = index;
					index = index + 1;
	#now every thresholded region should have a bin number. Now we union find...
	#create array to map regions to eachother.
	#for example, 1 maps to 1, 2 maps to 2 and so on for now. if bins[3] = 5, we can say "3 maps to 5"
	bins = [0] *index;
	for i in range(0, index):
		bins[i] = i;

	#find mappings
	for r in range(0,row):
		for c in range(0, col):
			if(raster[r][c] != 0):
				if(r != 0 and c != 0 and raster[r-1][c] != 0 and raster[r][c-1] != 0):
					minimum = min(raster[r-1][c], raster[r][c-1], raster[r][c])
					bins[raster[r-1][c]] = minimum;
					bins[raster[r][c-1]] = minimum;
					bins[raster[r][c]]   = minimum;
				elif(r != 0 and raster[r-1][c] != raster[r][c] and raster[r-1][c] != 0):
					minimum = min(raster[r-1][c], raster[r][c]);
					bins[raster[r][c]]   = minimum;
					bins[raster[r-1][c]] = minimum;
				elif(c != 0 and raster[r][c-1] != raster[r][c] and raster[r][c-1] != 0):
					minimum = min(raster[r][c-1], raster[r][c]);
					bins[raster[r][c]]   = minimum;
					bins[raster[r][c-1]] = minimum;

	#compute union of groups
	for r in range(0,row):
		for c in range(0, col):
			if(raster[r][c] != 0):
				raster[r][c] = bins[raster[r][c]];

	return raster

def angle(img, debug):
	(row, col) = img.shape;
	
	mean  = 0.0;
	count = 0.0;
	midrow = row;
	midcol = col/2;
	if debug:
		img_test = (img == 0)*0;
		img_test = img_test.astype('uint8');

	for r in range(0, row):
		avg_col = 0;
		cnt_col = 0;
		if(sum(img[r][:]) != 0):
			for c in range(0, col):
				if(img[r][c] != 0):
					avg_col += c;
					cnt_col += 1;
			avg_col = avg_col / cnt_col;
			if debug:
				img_test[r][int(avg_col)] = 255;
			mean  += (midcol - avg_col);
			count += 1;
	if count == 0:
		mean = 0;
	else:
		mean = mean / count;
		mean = mean / row;
	if debug:
		return (img_test, mean);
	else:
		return mean;

#this function has NOT been tested
def largest_bin(img):
	freq = stats.itemfreq(img.squeeze());
	arg_max = np.argmax(freq[:][1]);
	bin_max = freq[arg_max][0];
	print bin_max
	print arg_max









