

# Python program to read image using PIL module
  
# importing PIL
from PIL import Image
  
# Read image
I=Image.open("x2.png")
print('Size of Image',I.size)  
Image.open("x2.png")

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
img = mpimg.imread("x2.png")
plt.imshow(img)
plt.show()

from PIL import Image
import cv2
from google.colab.patches import cv2_imshow
img = cv2.imread("x2.png") 
cv2_imshow(img)

import skimage.io as io
image = io.imread("x2.png")

io.imshow(image)

from PIL import Image 
import PIL 
im1 = Image.open("x2.png") 
im1 = im1.save("x11.png")

Image.open("x11.png")

import matplotlib.pyplot as plt
x = [0, 2, 4, 6]
y = [1, 3, 4, 8]

plt.plot(x,y)

plt.xlabel('x values')
plt.ylabel('y values')
plt.title('plotted x and y values')
plt.legend(['line 1'])

# save the figure
plt.savefig('plot.png', dpi=300, bbox_inches='tight')

plt.show()

import cv2 as cv2 
from google.colab.patches import cv2_imshow
image = cv2.imread("x2.png")

cv2_imshow(image) 
filename = 'savedImage.jpg'

cv2.imwrite(filename,image[:,:50,:25])


img = cv2.imread('savedImage.jpg') 
cv2_imshow(img)

"""

> 


"""

# importing required library
import skimage.io as io

#image = io.imread("http://host.robots.ox.ac.uk/pascal/VOC/images/voc2005_11c.jpg")
image = io.imread("x2.png")

import matplotlib.pyplot as plt
io.imshow(image)

#Check the image matrix data type (could know the bit depth of the image)
print(image.dtype)
# Check the height of image 
print(image.shape[0])
# Check the width of image 
print(image.shape[1])
# Check the number of channels of the image
print(image.shape[2])

from PIL import Image

im = Image.open("x1.png")
width, height = im.size

# Display height and width
print(width)
print(height)

# print the filename
print(im.filename)

# print the format of the image
print(im.format) 

# print the format description of the image
print(im.format_description)

# importing all the required libraries
import skimage.io as io

from skimage.transform import rotate

import numpy as np
import matplotlib.pyplot as plt

image = io.imread("x2.png")

def image_augment(image):
    fig,ax = plt.subplots(nrows=1,ncols=3,figsize=(15,8))
    ax[0].imshow(image)
    ax[0].axis('off')
    ax[1].imshow(rotate(image, angle=45, mode = 'wrap'))
    ax[1].axis('off')
    ax[2].imshow(np.fliplr(image))
    ax[2].axis('off')

# Apply on an image
image_augment(image)

import cv2 
from google.colab.patches import cv2_imshow # for image display

image = cv2.imread("x2.png")
cv2_imshow(image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray_image)

"""

---















####7.3.2.2 Converting images from BGR to RGB ."""

import numpy as np
import pandas as pd
import cv2 as cv 
from google.colab.patches import cv2_imshow # for image display
from skimage import io
from PIL import Image # Pillow library 
import matplotlib.pylab as plt

# Create a list to store the urls of the images
urls = ["https://iiif.lib.ncsu.edu/iiif/0052574/full/800,/0/default.jpg", 
        "https://iiif.lib.ncsu.edu/iiif/0016007/full/800,/0/default.jpg", 
        "https://placekitten.com/800/571"]  
# Read and display the image, # loop over the image URLs, you could store several image urls in the list

images=[]
for url in urls:
  image = io.imread(url) 
  images.append(io.imread(url))
  image_2 = cv.cvtColor(image, cv.COLOR_BGR2RGB)
  final_frame = cv.hconcat((image, image_2))
  cv2_imshow(final_frame)
  print('\n')

"""### Post Lab Exercise

#### Problem 1 Load a image from url and and print shape and format of image.
"""

import numpy as np
import pandas as pd
import cv2 as cv
from google.colab.patches import cv2_imshow
from skimage import io
from PIL import Image
import matplotlib.pylab as plt
urls = ["http://staffmobility.eu/sites/default/files/isewtweetbg.jpg"]
images=[]
for url in urls:
  image = io.imread(url)
  images.append(io.imread(url))
  cv2_imshow(image)
  print("The shape of the image is",image.shape)

"""
#### Problem 2 Load a image from Google drive and and rotate image by 45 degree and display both images."""

import skimage.io as io
from skimage.transform import rotate
import numpy as np
import matplotlib.pyplot as plt
image=io.imread("x2.png")
def image_augment(image):
  fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(15,8))
  ax[0].imshow(image)
  ax[0].axis('off')
  ax[1].imshow(rotate(image, angle=45, mode='wrap'))
  ax[1].axis('off')
image_augment(image)

"""Problem 3 Load at least three colour images and convert them into grayscale. Display originalimages as well as images in grayscale format."""

import cv2
from google.colab.patches import cv2_imshow
image = cv2.imread("x2.png")
image1 = cv2.imread("x4.png")
image2 = cv2.imread("x5.png")
img=cv2.resize(image,(300,240))
img1=cv2.resize(image1,(300,240))
img2=cv2.resize(image2,(300,240))
cv2_imshow(img)
cv2_imshow(img1)
cv2_imshow(img2)
gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_image1=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_image2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray_img=cv2.resize(gray_image,(300,240))
gray_img1=cv2.resize(gray_image1,(300,240))
gray_img2=cv2.resize(gray_image2,(300,240))
cv2_imshow(gray_img)
cv2_imshow(gray_img2)
cv2_imshow(gray_img2)
