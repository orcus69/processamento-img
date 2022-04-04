import cv2
import numpy as np

img = cv2.imread('../logo-if.jpg')

cv2.imshow('logo-if', img)

##original height and width
(height, width) = img.shape[0:2]

#new height and width
low_width = int(width/3)
low_height = int(height/3)

#new image
result = np.zeros((low_height, low_width, 3), np.uint8)

for x in range(0, low_height):
    for y in range(0, low_width):
        result[x,y] = img[x*3+1, y*3+1]

cv2.imshow('low-quality', result)

cv2.waitKey(0)
cv2.destroyAllWindows()