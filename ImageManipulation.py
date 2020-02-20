from PIL import Image
import math
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  image.save(path, 'png')

# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel
# Create a Grayscale version of the image
def convert_grayscale(image):
  # Get size
  width, height = image.size

  # Create new Image and a Pixel Map
  new = create_image(width, height)
  pixels = new.load()

  # Transform to grayscale
  for i in range(width):
    for j in range(height):
      # Get Pixel
      pixel = get_pixel(image, i, j)

      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

      # Transform to grayscale
      gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

      # Set Pixel in new image
      pixels[i, j] = (int(gray), int(gray), int(gray))

    # Return new image
    return new

image = open_image('/home/mike/Mike/python/grbpwr.png')
WhiteImage = create_image(2335,2335)
for x in range(2335):
    for y in range(2335):
      WhiteImage.putpixel((x,y),(0,0,0,255))

for x in range(2335):
    for y in range(2335):
        x1 = (2*x-2335)/2335.0
        y1 = (2*y-2335)/-2335.0
        x1 = x1*math.sqrt((1-y1**2)/2)
        y1=y1*math.sqrt((1-x1**2)/2)
        x1=int(math.floor(x1*2335/2+2335/2))
        y1=int(math.floor(-y1*2335/2+2335/2))
        color1 = get_pixel(image,x,y)[0]
        color2 = get_pixel(image,x,y)[1]
        color3 = get_pixel(image,x,y)[2]
        if(color1 == 0 & color2 == 0 & color3 == 0):
          color1 = 0
          color2 = 0
          color3 = 0
        WhiteImage.putpixel((x1,y1),(color1,color2,color3,255))
save_image(WhiteImage,'/home/mike/Mike/python/whiteimage')