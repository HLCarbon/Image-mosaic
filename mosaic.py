import functions as fc
import glob
import sys
from PIL import Image
import copy

#sets the path for the desired image and for all the other images
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

#Taking into account the number of photos we have in the folder with all the iamages, it resizes the desired image so it can fit the most amount of 
#images. The returned shape is as close as the original photo as it can be. It also returns the number of photos that the final image will have
#on the x axis, on the y axis and the new shape of the photo.
x,y,shape,resized_desired_image = fc.new_shape(desired_image, len(initial_photos))
#transforms the desired image into an array.
array_desired_image = fc.reshape_photo_to_array(resized_desired_image)
#reshapes all the other photos into smaller ones so they can fit into the big image.
new_photos = fc.reshape_all_photos(initial_photos, shape, x, y)
#joins all the small photos into one big photo with the size of the desired photo.
joined_photo = fc.create_joined_photo(array_desired_image, new_photos, shape, x, y)
#joins the desired image with the new photo containing all the small ones. The desired photo has a weight of 0.7 and the other photo a weight of 1-0.7 = 0.3.
final = fc.create_photo(array_desired_image, joined_photo, 0.7)
#saves the new joined photo and the final photo.
fc.save_image(joined_photo, 'joined')
fc.save_image(final, 'final')



