from PIL import Image
import os, sys

path = ("../goodRotated/")

for i in range(1,684):
    for item in os.listdir(path):
        if os.path.isfile(path+item):
            script_dir = os.path.dirname(os.path.abspath("../goodRotated/"+__file__))
            im = Image.open(os.path.join(script_dir, item)) #create image object
            file, ext = os.path.splitext(item)
            new_img = im.resize((256,256))
            new_img.save(file + 'Resized.png', 'PNG', quality=90)
