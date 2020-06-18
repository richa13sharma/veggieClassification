import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle
from keras.utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from model import Model_CNN
from keras.models import load_model


def create_training_data():
    for category in CATEGORIES: 
        path = os.path.join(DATADIRT,category)  #create path 
        class_num = CATEGORIES.index(category)  #get the classification 0=good 1=ugly
        for img in os.listdir(path):  # iterate over each image in each folder
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num]) 
            except Exception as e:  
                pass
    # print("TRAIN",len(training_data))

def create_validation_data():
    for category in CATEGORIES: 
        path = os.path.join(DATADIRV,category)  #create path 
        class_num = CATEGORIES.index(category)  #get the classification 0=good 1=ugly
        for img in os.listdir(path):  #iterate over each image in each folder
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                # print(img_array.shape)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                validation_data.append([new_array, class_num]) 
            except Exception as e:  
                pass
    # print("VAL",len(validation_data))


DATADIRT = 'data/train/'
DATADIRV = 'data/validate/'
CATEGORIES = ['good','ugly']
IMG_SIZE = 256

EPOCHS = 5
INIT_LR = 0.01
batchSize = 32
IMAGE_DIMS = (256, 256, 1) 

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
y_train = np.array(y_train)

#FOR TESTING DATA
for features,label in validation_data:
    X_test.append(features)
    y_test.append(label)
# print(len(X_test))

X_test = np.array(X_test).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
y_test = np.array(y_test)

# X_train = np.array(X_train, dtype="float") / 255.0
# X_test = np.array(X_test, dtype="float") / 255.0

y_train = to_categorical(y_train,2)
y_test = to_categorical(y_test,2)

#Pickle files for ref
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
'''
print("[INFO] Opening pickles")
X_train=pickle.load(open("X_train.pickle","rb"))
X_test=pickle.load(open("X_test.pickle","rb"))
y_train=pickle.load(open("y_train.pickle","rb"))
y_test=pickle.load(open("y_test.pickle","rb"))
'''

datagen = ImageDataGenerator(rescale=1./255)

print("[INFO] Done creating X and y")

# initialize the model using a sigmoid activation as the final layer for binary classification
print("[INFO] building model...")
model = Model_CNN.build(
	width=IMAGE_DIMS[1], height=IMAGE_DIMS[0],
	depth=IMAGE_DIMS[2], classes=2,
	finalAct="sigmoid")
# model = load_model('model23_3_2')
# initialize the model and optimizer 
print("[INFO] compiling network...")
opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)

model.compile(loss="binary_crossentropy", optimizer=opt,
	metrics=["binary_accuracy"])

train_generator = datagen.flow(X_train, y_train, batch_size=batchSize, seed = 42)
test_generator = datagen.flow(X_test, y_test, batch_size=batchSize, seed = 42)
# train the network
print("[INFO] training network...")
H = model.fit_generator(
    train_generator,
	validation_data= test_generator,
	steps_per_epoch=len(X_train) // batchSize,
	epochs=EPOCHS, verbose=1)

#Saving model
print("[INFO] serializing network ...")
model.save_weights("modelreg1.h5")
model.save("modelreg1")

print("[INFO] summary ...")
print(model.summary())


