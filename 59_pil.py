from PIL import Image

with Image.open("fishman.bmp") as im:

	w, h = im.size
	print("Original image size: %sx%s" % (w, h))

	im.thumbnail((w//3, h//3))
	print("Resize image to: %sx%s" % (w//3, h//3))
	im.save("thumbnail.jpg", "jpeg")


from PIL import ImageFilter
with Image.open('thumbnail.jpg') as im:
	im2 = im.filter(ImageFilter.BLUR)
	im2.save("blur.jpg", "jpeg")