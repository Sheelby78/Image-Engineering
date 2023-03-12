import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = (18, 10)
image = cv.imread("images/example.png",)

values = [
    [0.393, 0.769, 0.189],
    [0.349, 0.689, 0.168],
    [0.272, 0.534, 0.131],
]

image2 = image.reshape((-1,3))
image2 = np.float32(image2)
image2 /= 255

converted_image = []

for row in image2:
    converted_row = np.matmul(values, row.reshape(3,1))
    converted_image.append(converted_row.reshape(1,3))

converted_image = np.clip(converted_image, 0.0, 1.0)
converted_image = converted_image.reshape(image.shape)

plt.imshow(converted_image)
plt.show()