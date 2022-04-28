# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('../noise.jpg')
median = cv2.medianBlur(img,5)

cv2.imshow('Img',img)
cv2.imshow('Median Filter',median)

cv2.waitKey(0)
cv2.destroyAllWindows()