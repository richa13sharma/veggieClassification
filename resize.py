from PIL import Image
import os, sys

path = ("./dataset/GoodCarrotsCropped/finalGoodRotated/")

def resize():
    for item in os.listdir(path):
        if os.path.isfile(path+item):
            script_dir = os.path.dirname(os.path.abspath("./dataset/GoodCarrotsCropped/finalGoodRotated/"+__file__))
            im = Image.open(os.path.join(script_dir, item))
            im = im.convert("RGBA")
            f, e = os.path.splitext(item)
            imResized = im.resize((640,480), Image.ANTIALIAS)
            imResized.save(f + 's.png', 'PNG', quality=90)

resize()