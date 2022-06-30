from turtle import width
import numpy as np
import glob
from PIL import Image
import os
photos_path = 'all_images//*'
desired_image_path = 'desired_image//*'

#get desired_image

desired_image = Image.open(glob.glob(desired_image_path)[0])

#get other photos

'''initial_photos = []
for file in glob.glob(photos_path):
    initial_photos.append(Image.open(file))'''

def reshape_array(photo):
    width, height = photo.size
    photo2d_array = np.array(photo.getdata())
    image_array = []
    for y in range(height):
        image_array.append(photo2d_array[width*y:width*(y+1)])
    image_array = np.array(image_array)
    print('The new shape is:',image_array.shape)
    return image_array



def new_shape(desired_image, n_photos):
    width, height = desired_image.size
    proportion = width/height
    square = n_photos**(1/2)
    x = int(square*proportion)
    y = int(square*1/proportion)
    print(f'The number of images you are goin to use is {(x, y)}.')
    new_shape = (int(width/x)*x, int(height/y)*y)
    print('New size is', new_shape)
    return desired_image.resize(new_shape)

print(desired_image.size)
new_shape(desired_image, 999)



