from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

def rndChar():
	return chr(random.randint(65, 90))

def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# set size 240 * 4
width = 60 * 4
height = 60

# create a blank image
image = Image.new("RGB", (width, height), (255, 255, 255))

# create a font object
font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 36)

# create a draw object, related to image object 
draw = ImageDraw.Draw(image)

# fill px with rndColor()
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill = rndColor())

# create 4 words
for t in range(4):
	draw.text((60 * t + 10, 10), rndChar(), font = font, fill = rndColor2())

# blur it
image = image.filter(ImageFilter.BLUR)
image.save("code.jpg", "jpeg")