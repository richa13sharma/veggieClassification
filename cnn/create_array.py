import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle

def create_training_data():
    for category in CATEGORIES: 
        path = os.path.join(DATADIRT,category)  #create path 
        class_num = CATEGORIES.index(category)  #get the classification 0=good 1=ugly
        for img in os.listdir(path):  # iterate over each image in each folder
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                new_array = cv2.resize(img_array, (IMGSIZE, IMGSIZE))
                training_data.append([new_array, class_num]) 
            except Exception as e:  
                pass
    # print(len(training_data))

def create_validation_data():
    for category in CATEGORIES: 
        path = os.path.join(DATADIRV,category)  #create path 
        class_num = CATEGORIES.index(category)  #get the classification 0=good 1=ugly
        for img in os.listdir(path):  #iterate over each image in each folder
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                # print(img_array.shape)
                new_array = cv2.resize(img_array, (IMGSIZE, IMGSIZE))
                validation_data.append([new_array, class_num]) 
            except Exception as e:  
                pass
    # print(len(validation_data))


DATADIRT = 'data/train/'
DATADIRV = 'data/validate/'
CATEGORIES = ['good','ugly']
IMG_SIZE = 256

training_data = []
validation_data = []

create_training_data()
create_validation_data()

random.seed(42)
random.shuffle(training_data)
random.shuffle(validation_data)

X_train = []
X_test = []
y_train = []
y_test = []

#FOR TRAINING DATA
for features,label in training_data:
    X_train.append(features)
    y_train.append(label)
# print(len(X_train))
X_train = np.array(X_train).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
y_train = np.array(y_test)

#FOR TESTING DATA
for features,label in validation_data:
    X_test.append(features)
    y_test.append(label)
# print(len(X_test))
X_test = np.array(X_test).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
y_test = np.array(y_test)

pickle_out=open("X_train.pickle","wb")
pickle.dump(X_train,pickle_out)
pickle_out.close()

pickle_out=open("X_test.pickle","wb")
pickle.dump(X_test,pickle_out)
pickle_out.close()

pickle_out=open("y_train.pickle","wb")
pickle.dump(y_train,pickle_out)
pickle_out.close()

pickle_out=open("y_test.pickle","wb")
pickle.dump(y_test,pickle_out)
pickle_out.close()