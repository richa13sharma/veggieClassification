import keras
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=23,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        brightness_range=[0.2,1.0],
        fill_mode='nearest',
        )

img = load_img('grf662Resized.png')  # this is a PIL image
x = img_to_array(img)  # this is a Numpy array with shape (256,256,3)
# print(x.shape)
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1,256,256,3)
# print(x)

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `save_here/` directory
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='save_here', save_prefix='g662', save_format='png'):
    i += 1
    if i > 20:
        break  # otherwise the generator would loop indefinitely

