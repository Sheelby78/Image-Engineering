import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = (18, 10)
image = cv.imread("images/example.png",)

values = [
    [0.229, 0.587, 0.114],
    [0.500, -0.418, -0.082],
    [-0.168, -0.331, 0.500],
]

to_sum = [
    [0],
    [128],
    [128],
]

image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image2 = image.reshape((-1,3))

converted_image = []

for row in image2:
    converted_row = np.matmul(values, row.reshape(3,1))
    converted_row = np.add(to_sum, converted_row)
    converted_image.append(converted_row.reshape(1,3))

converted_image = np.clip(converted_image, 0, 255)
converted_image = np.asarray(converted_image)
converted_image = converted_image.reshape(image.shape)


fig, ax = plt.subplots(2, 2)

ax[0,0].imshow(image)
ax[0,1].imshow(converted_image[:, :, 0], cmap="Greys_r")
ax[1,0].imshow(converted_image[:, :, 2], cmap="Greys_r")
ax[1,1].imshow(converted_image[:, :, 1], cmap="Greys_r")

plt.show()