
from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
import numpy
import sys
import csv
import os
from os import path
numpy.set_printoptions(threshold=sys.maxsize)


for i in range(1,685):
    path1 = './dataset/uglyRotated/urf{0}.png'.format(i)
    if (path.exists(path1)):
        img = imread('./dataset/uglyRotated/urf{0}.png'.format(i))
    
        resized_img = resize(img, (128,64))
        
        fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True, multichannel=True) # orientations = number of bins for histogram
        
        fdlist = fd.tolist() 
    
        hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

        res = fdlist
        csvfile = './uglyrotatedHog.csv'

        with open(csvfile, mode='a') as output:
            writer = csv.writer(output)
            writer.writerow(res)
            # writer.writerow([])
    else:
        continue