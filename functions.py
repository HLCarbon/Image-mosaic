from attr import Attribute
import numpy as np
from PIL import Image
import sys




def reshape_photo_to_array(photo:Image.Image) ->np.array:
    width, height = photo.size
    photo = photo.convert('RGB')
    photo2d_array = np.array(photo.getdata())
    image_array = []
    for y in range(height):
        image_array.append(photo2d_array[width*y:width*(y+1)])
    image_array = np.array(image_array)
    #print('The new shape is:',image_array.shape)
    return image_array

def new_shape(desired_image: Image.Image, n_photos:int) ->(int,int,tuple,Image.Image):
    width, height = desired_image.size
    proportion = width/height
    square = n_photos**(1/2)
    x = int(square*proportion)
    y = int(square*1/proportion)
    print(f'The number of images you are going to use is {(x, y)}.')
    shape = (int(width/x)*x, int(height/y)*y)
    print('New size is', shape)
    return x,y,shape,desired_image.resize(shape)



def reshape_all_photos(initial_photos:list, shape:tuple, x:int, y:int)-> np.array:
    photos_in_array = []
    n = 0
    for image in initial_photos:
        print('Photo number:\n',n)
        n_shape = (int(shape[0]/x),int(shape[1]/y))
        try:
            image_reshape = image.resize(n_shape)
        except AttributeError:
            print('meh')
            image_reshape = Image.new("RGB", (500,500), (255, 255, 255))
        image_array = reshape_photo_to_array(image_reshape)
        
        photos_in_array.append(image_array)
        n +=1
    return np.array(photos_in_array)

def create_joined_photo(desired_photo:Image.Image, array_of_photos:np.array, shape:tuple, x:int, y:int)->np.array:

    n_for_x = int(shape[0]/x)
    n_for_y = int(shape[1]/y)

    new_photo = desired_photo.copy()

    for a in range(x):
        for b in range(y):
            for c in range(n_for_y):
                new_photo[b*n_for_y+c][(n_for_x)*a:(a+1)*(n_for_x)] = array_of_photos[b*x+a][c]
    return new_photo

def create_photo(photo:np.array, joined_photos:np.array, proportion:float)->np.array:
    final = photo*proportion + joined_photos*(1-proportion)
    return final

def save_image(image:np.array, file_name:str) -> None:
    final_array = final_array.astype(np.uint8)
    new_image = Image.fromarray(final_array)
    new_image.save(f'final_image/{file_name}.png')
    print('Your image was saved!')
