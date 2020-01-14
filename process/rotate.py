from PIL import Image
import os, sys

# path = ("./dataset/GoodCarrotsCropped/")
path = ("./dataset/UglyCarrots/")

def rotate():
    for item in os.listdir(path):
        if os.path.isfile(path+item):
            if item == path + '.DS_Store':
                continue
            script_dir = os.path.dirname(os.path.abspath("./dataset//UglyCarrots/"+__file__))
            im = Image.open(os.path.join(script_dir, item)) #create image object
            file, ext = os.path.splitext(item)
            angle90 = 90
            angle180 = 180
            angle45 = 45
            # imRotate90 = im.rotate(angle90 , expand = 'true' , fillcolor = 'white')
            # imRotate90.save(file + 'Rotated90.png', 'PNG', quality=90)
            imRotate45 = im.rotate(angle45 , expand = 'true' , fillcolor = 'white')
            imRotate45.save(file + 'Rotated45.png', 'PNG', quality=90)
            # imRotate180 = im.rotate(angle180 , expand = 'true' , fillcolor = 'white')
            # imRotate180.save(file + 'Rotated180.png', 'PNG', quality=90)
            
        
rotate()