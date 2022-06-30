import functions as fc
import glob
from PIL import Image
photos_path = 'all_images//*'
desired_image_path = 'desired_image//*'



#get desired_image

desired_image = Image.open(glob.glob(desired_image_path)[0])

#get other photos

initial_photos = []
for file in glob.glob(photos_path):
    initial_photos.append(Image.open(file))

x,y,shape,resized_desired_image = fc.new_shape(desired_image, 999)
array_desired_image = fc.reshape_photo_to_array(resized_desired_image)
new_photos = fc.reshape_all_photos(initial_photos, shape, x, y)
joined_photo = fc.create_joined_photo(array_desired_image, new_photos, shape, x, y)
final = fc.create_photo(array_desired_image, joined_photo, 0.7)
fc.save_image(joined_photo, 'joined_photos')
fc.save_image(array_desired_image,  'original_photo')
fc.save_image(final, 'final')



