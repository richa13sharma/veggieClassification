from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
import numpy
import sys
import csv
import pandas as pd
numpy.set_printoptions(threshold=sys.maxsize)

data = pd.read_csv("data.csv")
list1 = []
for i in range(1,480):
    list1.append('good')
for i in range(1,685):
    list1.append('ugly')
print(data)
data.insert(3781, column='good', value=list1)
# data.drop(data.columns[0], axis=1)
data.to_csv('./data.csv')
print(data)