from PIL import Image
from PIL import ImageDraw

width = 400
height = 400

img = Image.new("RGBA", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(img)
for i in range(int(width / 20 + 1)):
    draw.rectangle((10 * (2 * i - 2), 0, 10 * (2 * i - 1), height), fill='red')
    draw.rectangle((10 * (2 * i - 1), 0, 10 * (2 * i), height), fill='blue')

img.save("test.png")
