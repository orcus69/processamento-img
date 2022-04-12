# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('../logo-if.jpg')

rows,cols = img.shape[:2]

RED = (0, 0, 255)

rotate = 0
col, row = 0, 0

def rotation():
    global rotate
    rotate = rotate + 1

#set a point with mouse
def set_point(event, x, y, flags, param):
    global col, row
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,RED,-1)
        col, row = x,y

cv2.namedWindow('logo-if')
cv2.setMouseCallback('logo-if', set_point)

while(1):
    result = cv2.getRotationMatrix2D((col, row),rotate,1)
    res = cv2.warpAffine(img,result,(cols,rows))

    cv2.imshow('logo-if',res)

    k=cv2.waitKey(20)
    if k == ord('a'):
        rotation()
        print(rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()