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

def determine_number_photos(desired_image, n_photos):
    width, height = desired_image.size
    proportion = width/height
    for i in range(int((n_photos)**(1/2))):
        number = int((n_photos)**(1/2))-i
        photos_for_x = number
        photos_for_y = photos_for_x*(1/proportion)
        if photos_for_y.is_integer():
            print(f'You need to use {number} photos.')
            return(desired_image)
    shape = (int((n_photos)**(1/2)), int(int((n_photos)**(1/2))*(1/proportion) ))
    desired_image = desired_image.resize(shape)
    print(f'Your image was resized to {shape}.')

determine_number_photos(desired_image, 999)


#new = reshape_array(desired_image)



