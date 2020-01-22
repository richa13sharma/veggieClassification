from PIL import Image
import os, sys

#path = ("../dataset/GoodCarrotsCropped/")
path = ("../dataset/UglyCarrots/")

def rotate():
    for item in os.listdir(path):
        if os.path.isfile(path+item):
            if item == path + '.DS_Store':
                continue
            #script_dir = os.path.dirname(os.path.abspath("../dataset/GoodCarrotsCropped/"+__file__))
            script_dir = os.path.dirname(os.path.abspath("../dataset/UglyCarrots/"+__file__))
            im = Image.open(os.path.join(script_dir, item)) #create image object
            file, ext = os.path.splitext(item)
            angle180 = 180
            # imRotate180 = im.rotate(angle180 , expand = 'true' , fillcolor = 'white')
            # imRotate180.save(file + 'Rotated180.png', 'PNG', quality=90)
            for degree in range(30,361,30):
                imRotate= im.rotate(degree , expand = 'true' , fillcolor = 'white')
                i = str(degree)
                imRotate.save(file + 'URotated'+i+'.png', 'PNG', quality=90)
                #print("saved")
            
        
rotate()