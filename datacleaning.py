from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
import numpy
import sys
import csv
import pandas as pd
import re
numpy.set_printoptions(threshold=sys.maxsize)

def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString

def removeDecimal():
    with open("./goodAfterHog.csv", 'rt') as f:
        data = csv.reader(f)
        list1 = []
        for row in data:
            i = 1
            while i != 3780:
                count = 0
                len1 = len(row[i])
                j = 0
                while (j < len1):
                    # print(row[i])
                    # print(len(row[i]))
                    if (row[i][j].__contains__('.')):
                        count += 1
                        # print(count)
                    if (count >= 2):
                        row[i] = replacenth(row[i], '.', '', 3)
                        print("Decimal removed")
                        len1 = len1 - 1
                        j -= 1
                        break
                    j += 1
                i += 1
            list1.append(row)
    o = open('data1.csv', 'w')
    with o:
        writer = csv.writer(o)
        for rows in list1:
            writer.writerow(rows)

def removeE():
    with open("./data1.csv", 'rt') as f:
        data = csv.reader(f)
        list2 = []
        count = 0
        for row in data:
            i = 1
            while i != 3780:
                print(row[i])
                # print(i)
                # print(len(row[i]))
                if (row[i].__contains__('e')):
                    row[i] = float(row[i])
                i += 1
            list2.append(row)
        print("count ",count)
    o = open('data2.csv', 'w')
    with o:
        writer = csv.writer(o)
        for rows in list2:
            writer.writerow(rows)

removeDecimal()
removeE()