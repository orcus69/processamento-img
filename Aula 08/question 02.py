# coding=utf-8
import cv2
import numpy as np

ksize=9

#images
background = cv2.imread('../cars.png')

mask = np.ones(background.shape, np.uint8)
cv2.circle(mask, (mask.shape[1] - 480, mask.shape[0] - 300), 200, (255, 255, 255), -1)
mask = cv2.GaussianBlur(background,(ksize,ksize),0)

#black circle
mask_inv = cv2.bitwise_not(mask)
#bluring mask
gauss = cv2.GaussianBlur(background,(ksize,ksize),0)

blur = gauss * (mask_inv / 255)
focus = background * ( mask / 255 )


img = cv2.add(blur, focus, dtype=cv2.CV_8U)
cv2.imshow('overlay',img)
#cv2.imshow('mask_inv',blur)
#cv2.imshow('mask_isnv',focus)
cv2.waitKey(0)

cv2.destroyAllWindows()