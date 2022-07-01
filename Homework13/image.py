from PIL import Image

im1 = Image.open('sample_image.jpg')
print("Mode of the image: {}".format(im1.mode))
print("Size of the image: {}".format(im1.size))
print("Format of the image: {}".format(im1.format))

im1.thumbnail((128,128))
im1.save('sample_image_thumb.png')
im1.show()
