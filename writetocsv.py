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

data = pd.read_csv("cuglyHogcopy.csv")
list1 = []
for i in range(0,1606):
    list1.append('ugly')
#for i in range(1,685):
   # list1.append('ugly')
print(data.head())
data.insert(3780, "ugly", value="ugly", allow_duplicates=False)
# data.drop(data.columns[0], axis=1)
data.to_csv('./dataUgly.csv')
print(data)

