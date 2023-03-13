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

converted_image = np.asarray(converted_image)
converted_image = np.clip(converted_image, 0, 255)
converted_image = converted_image.reshape(image.shape)

Y = []
Cb = []
Cr = []


for i in range(len(converted_image)):
    Y_help = []
    Cb_help = []
    Cr_help = []
    for j in range(len(converted_image[0])):
        Y_help.append(converted_image[i][j][0])
        if i % 2 == 0 and j % 2 == 0:
            Cb_help.append(converted_image[i][j][1])
            Cr_help.append(converted_image[i][j][2])
    Y.append(Y_help)
    if Cb_help:
        Cb.append(Cb_help)
        Cr.append(Cr_help)

up_scaled = converted_image.copy()

Cb_up = []
Cr_up = []
for i in range(len(Cb)):
    Cb_help = []
    Cr_help = []
    for j in range(len(Cb[i])):
        Cb_help.append(Cb[i][j])
        Cb_help.append(Cb[i][j])
        Cr_help.append(Cr[i][j])
        Cr_help.append(Cr[i][j])
    Cb_up.append(Cb_help)
    Cb_up.append(Cb_help)
    Cr_up.append(Cr_help)
    Cr_up.append(Cr_help)

for i in range(len(converted_image)):
    for j in range(len(converted_image[0])):
        up_scaled[i][j][0] = Y[i][j]
        up_scaled[i][j][1] = Cb_up[i][j]
        up_scaled[i][j][2] = Cr_up[i][j]


up_scaled = np.asarray(up_scaled)
up_scaled = up_scaled.astype(np.uint8)
up_scaled = up_scaled.reshape(image.shape)
up_scaled = cv.cvtColor(up_scaled, cv.COLOR_YCrCb2RGB)

fig, ax = plt.subplots(2, 2)

ax[0,0].imshow(up_scaled)
ax[0,1].imshow(converted_image[:, :, 0], cmap="Greys_r")
ax[1,0].imshow(converted_image[:, :, 2], cmap="Greys_r")
ax[1,1].imshow(converted_image[:, :, 1], cmap="Greys_r")

plt.show()