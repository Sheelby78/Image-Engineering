import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = (18, 10)

image = cv.imread("images/example.jpg")

kernel = [
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1],
]

kernel = np.asarray(kernel)
filtered_image = cv.filter2D(image, -1, kernel=kernel)

plt.imshow(filtered_image)

plt.show()
print(type(image), image.shape)

