from turtle import width
import numpy as np
import glob
from PIL import Image
import os
photos_path = 'all_images//*'
desired_image_path = 'desired_image//*'



def reshape_photo_to_array(photo):
    width, height = photo.size
    photo = photo.convert('RGB')
    photo2d_array = np.array(photo.getdata())
    image_array = []
    for y in range(height):
        image_array.append(photo2d_array[width*y:width*(y+1)])
    image_array = np.array(image_array)
    #print('The new shape is:',image_array.shape)
    return image_array

def new_shape(desired_image, n_photos):
    width, height = desired_image.size
    print(width, height)
    proportion = width/height
    square = n_photos**(1/2)
    x = int(square*proportion)
    y = int(square*1/proportion)
    print(f'The number of images you are going to use is {(x, y)}.')
    shape = (int(width/x)*x, int(height/y)*y)
    print('New size is', shape)
    return x,y,shape,desired_image.resize(shape)



def reshape_all_photos(initial_photos, shape, x, y):
    photos_in_array = []
    for image in initial_photos:
        n_shape = (int(shape[0]/x),int(shape[1]/y))
        image_reshape = image.resize(n_shape)
        image_array = reshape_photo_to_array(image_reshape)
        photos_in_array.append(image_array)
    return photos_in_array

def create_joined_photo(desired_photo, lst_of_photos, shape, x, y):

    n_for_x = int(shape[0]/x)
    n_for_y = int(shape[1]/y)

    new_photo = desired_photo

    for a in range(x):
        for b in range(y):
            for c in range(n_for_y):
                new_photo[b*n_for_y+c][(n_for_x)*a:(a+1)*(n_for_x)] = lst_of_photos[b*x+a][c]
    return new_photo

def save_image(image, size, file_name):
    final_lst = []
    for i in image:
        final_lst += list(i)
    final_array = np.array(final_lst)
    final_array = final_array.astype(int)
    new_image = Image.frombytes(mode = 'RGB', size = size, data = final_array)
    new_image.save(f'final_image/{file_name}.jpeg')
#get desired_image

desired_image = Image.open(glob.glob(desired_image_path)[0])

#get other photos

initial_photos = []
for file in glob.glob(photos_path):
    initial_photos.append(Image.open(file))

x,y,shape,resized_desired_image = new_shape(desired_image, 999)
array_desired_image = reshape_photo_to_array(resized_desired_image)
new_photos = reshape_all_photos(initial_photos, shape, x, y)

new_photo = create_joined_photo(array_desired_image, new_photos, shape, x, y)
save_image(new_photo, shape, 'joined_photos')
final = (new_photo + array_desired_image)/2
save_image(final, shape, 'final')
#print(final[0])


