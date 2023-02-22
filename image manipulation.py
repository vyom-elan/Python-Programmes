

import matplotlib.pyplot as plt

from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean

image = color.rgb2gray(data.astronaut())

image_rescaled = rescale(image, 0.25, anti_aliasing=False)
image_resized = resize(image, (image.shape[0] // 4, image.shape[1] // 4),
                       anti_aliasing=True)
image_downscaled = downscale_local_mean(image, (4, 3))

fig, axes = plt.subplots(nrows=2, ncols=2)

ax = axes.ravel()

ax[0].imshow(image, cmap='gray')
ax[0].set_title("Original image")

ax[1].imshow(image_rescaled, cmap='gray')
ax[1].set_title("Rescaled image (aliasing)")

ax[2].imshow(image_resized, cmap='gray')
ax[2].set_title("Resized image (no aliasing)")

ax[3].imshow(image_downscaled, cmap='gray')
ax[3].set_title("Downscaled image (no aliasing)")

ax[0].set_xlim(0, 512)
ax[0].set_ylim(512, 0)
plt.tight_layout()
plt.show()

#from google.colab import files
import cv2
import numpy as np
import matplotlib.pyplot as plt
#image=files.upload()
img=cv2.imread('lena.jpg')
#img = cv2.resize(img, (700,700))
matrix=np.ones(img.shape, dtype="uint8")*70
img_brighter=cv2.add(img,matrix)
img_darker=cv2.subtract(img,matrix)
plt.subplot(151); 
plt.imshow(img)
plt.title("og image")
plt.subplot(153);
plt.imshow(img_brighter)
plt.title("brighter image")
plt.subplot(155);
plt.imshow(img_darker)
plt.title("darker image");

import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage import gaussian_filter
from skimage import data
from skimage import img_as_float
from skimage.morphology import reconstruction
image = img_as_float(data.coins())
image = gaussian_filter(image, 1)

seed = np.copy(image)
seed[1:-1, 1:-1] = image.min()
mask = image

dilated = reconstruction(seed, mask, method='dilation')
plt.show()

fig, (ax0, ax1, ax2) = plt.subplots(nrows=1,
                                    ncols=3,
                                    figsize=(8, 2.5),
                                    sharex=True,
                                    sharey=True)

ax0.imshow(image, cmap='gray')
ax0.set_title('original image')
ax0.axis('off')

ax1.imshow(dilated, vmin=image.min(), vmax=image.max(), cmap='gray')
ax1.set_title('dilated')
ax1.axis('off')

ax2.imshow(image - dilated, cmap='gray')
ax2.set_title('image - dilated')
ax2.axis('off')

fig.tight_layout()

h = 0.4
seed = image - h
dilated = reconstruction(seed, mask, method='dilation')
hdome = image - dilated

fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3, figsize=(8, 2.5))
yslice = 197

ax0.plot(mask[yslice], '0.5', label='mask')
ax0.plot(seed[yslice], 'k', label='seed')
ax0.plot(dilated[yslice], 'r', label='dilated')
ax0.set_ylim(-0.2, 2)
ax0.set_title('image slice')
ax0.set_xticks([])
ax0.legend()

ax1.imshow(dilated, vmin=image.min(), vmax=image.max(), cmap='gray')
ax1.axhline(yslice, color='r', alpha=0.4)
ax1.set_title('dilated')
ax1.axis('off')

ax2.imshow(hdome, cmap='gray')
ax2.axhline(yslice, color='r', alpha=0.4)
ax2.set_title('image - dilated')
ax2.axis('off')

fig.tight_layout()
plt.show()

#mean filters
import matplotlib.pyplot as plt

from skimage import data
from skimage.morphology import disk
from skimage.filters import rank


image = data.coins()
selem = disk(20)

percentile_result = rank.mean_percentile(image, selem=selem, p0=.1, p1=.9)
bilateral_result = rank.mean_bilateral(image, selem=selem, s0=500, s1=500)
normal_result = rank.mean(image, selem=selem)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10),
                         sharex=True, sharey=True)
ax = axes.ravel()

titles = ['Original', 'Percentile mean', 'Bilateral mean', 'Local mean']
imgs = [image, percentile_result, bilateral_result, normal_result]
for n in range(0, len(imgs)):
    ax[n].imshow(imgs[n], cmap=plt.cm.gray)
    ax[n].set_title(titles[n])
    ax[n].axis('off')

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

from skimage import filters
from skimage.data import camera
from skimage.util import compare_images


image = camera()
edge_roberts = filters.roberts(image)
edge_sobel = filters.sobel(image)

fig, axes = plt.subplots(ncols=2, sharex=True, sharey=True,
                         figsize=(8, 4))

axes[0].imshow(edge_roberts, cmap=plt.cm.gray)
axes[0].set_title('Roberts Edge Detection')

axes[1].imshow(edge_sobel, cmap=plt.cm.gray)
axes[1].set_title('Sobel Edge Detection')

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()

x, y = np.ogrid[:100, :100]

# Creating a rotation-invariant image with different spatial frequencies.
image_rot = np.exp(1j * np.hypot(x, y) ** 1.3 / 20.).real

edge_sobel = filters.sobel(image_rot)
edge_scharr = filters.scharr(image_rot)
edge_prewitt = filters.prewitt(image_rot)

diff_scharr_prewitt = compare_images(edge_scharr, edge_prewitt)
diff_scharr_sobel = compare_images(edge_scharr, edge_sobel)
max_diff = np.max(np.maximum(diff_scharr_prewitt, diff_scharr_sobel))

fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True,
                         figsize=(8, 8))
axes = axes.ravel()

axes[0].imshow(image_rot, cmap=plt.cm.gray)
axes[0].set_title('Original image')

axes[1].imshow(edge_scharr, cmap=plt.cm.gray)
axes[1].set_title('Scharr Edge Detection')

axes[2].imshow(diff_scharr_prewitt, cmap=plt.cm.gray, vmax=max_diff)
axes[2].set_title('Scharr - Prewitt')

axes[3].imshow(diff_scharr_sobel, cmap=plt.cm.gray, vmax=max_diff)
axes[3].set_title('Scharr - Sobel')

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()

x, y = np.mgrid[-10:10:255j, -10:10:255j]
image_rotinv = np.sin(x ** 2 + y ** 2)

image_x = 2 * x * np.cos(x ** 2 + y ** 2)
image_y = 2 * y * np.cos(x ** 2 + y ** 2)

def angle(dx, dy):
    """Calculate the angles between horizontal and vertical operators."""
    return np.mod(np.arctan2(dy, dx), np.pi)


true_angle = angle(image_x, image_y)

angle_farid = angle(filters.farid_h(image_rotinv),
                    filters.farid_v(image_rotinv))
angle_sobel = angle(filters.sobel_h(image_rotinv),
                    filters.sobel_v(image_rotinv))
angle_scharr = angle(filters.scharr_h(image_rotinv),
                     filters.scharr_v(image_rotinv))
angle_prewitt = angle(filters.prewitt_h(image_rotinv),
                      filters.prewitt_v(image_rotinv))

def diff_angle(angle_1, angle_2):
    return np.minimum(np.pi - np.abs(angle_1 - angle_2),
                      np.abs(angle_1 - angle_2))


diff_farid = diff_angle(true_angle, angle_farid)
diff_sobel = diff_angle(true_angle, angle_sobel)
diff_scharr = diff_angle(true_angle, angle_scharr)
diff_prewitt = diff_angle(true_angle, angle_prewitt)

fig, axes = plt.subplots(nrows=3, ncols=2, sharex=True, sharey=True,
                         figsize=(8, 8))
axes = axes.ravel()

axes[0].imshow(image_rotinv, cmap=plt.cm.gray)
axes[0].set_title('Original image')

axes[1].imshow(true_angle, cmap=plt.cm.hsv)
axes[1].set_title('Analytical gradient angle')

axes[2].imshow(diff_sobel, cmap=plt.cm.inferno, vmin=0, vmax=0.02)
axes[2].set_title('Sobel error')

axes[3].imshow(diff_prewitt, cmap=plt.cm.inferno, vmin=0, vmax=0.02)
axes[3].set_title('Prewitt error')

axes[4].imshow(diff_scharr, cmap=plt.cm.inferno, vmin=0, vmax=0.02)
axes[4].set_title('Scharr error')

color_ax = axes[5].imshow(diff_farid, cmap=plt.cm.inferno, vmin=0, vmax=0.02)
axes[5].set_title('Farid error')

fig.subplots_adjust(right=0.8)
colorbar_ax = fig.add_axes([0.90, 0.10, 0.02, 0.50])
fig.colorbar(color_ax, cax=colorbar_ax, ticks=[0, 0.01, 0.02])

for ax in axes:
    ax.axis('off')

plt.show()
