import functions as fc
import glob
import sys
from PIL import Image
import copy

photos_path = sys.argv[0][:-9] + 'all_images//*'
desired_image_path = sys.argv[0][:-9] + 'desired_image//*'
#get desired_image

desired_image = Image.open(glob.glob(desired_image_path)[0])

#get other photos

initial_photos = []
for j in glob.glob(photos_path):
    for file in glob.glob(j):
        #The deep copy allows us to use a very large of photos as the background. If you try to open 10k+ images, you will receive an error.
        #This deep copy allows us to circunvent that.
        f = copy.deepcopy(Image.open(file))
        initial_photos.append(f)

x,y,shape,resized_desired_image = fc.new_shape(desired_image, len(initial_photos))
array_desired_image = fc.reshape_photo_to_array(resized_desired_image)
new_photos = fc.reshape_all_photos(initial_photos, shape, x, y)
joined_photo = fc.create_joined_photo(array_desired_image, new_photos, shape, x, y)
final = fc.create_photo(array_desired_image, joined_photo, 0.7)
fc.save_image(joined_photo, 'joined')
fc.save_image(final, 'final')



