# coding=utf-8
import cv2

#images
background = cv2.imread('../ifma-caxias.jpg')
logo = cv2.imread('../logo-if.jpg')

#resizing logo
logo = cv2.resize(logo,(200, 100),interpolation=cv2.INTER_AREA)

#initial position
rows,cols,channels = logo.shape
roi = background[0:rows, 0:cols ]

#creating mask
gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
ret, mask_inv = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask_inv)

#cutting background from logo
background_bg = cv2.bitwise_and(roi,roi, mask = mask_inv)
logo_fg = cv2.bitwise_and(logo,logo,mask = mask)

#logic operation AND to apply the overlay
dst=cv2.add(background_bg, logo_fg)
background[0:rows, 0:cols ] = dst

cv2.imshow('overlay',background)
cv2.waitKey(0)

cv2.destroyAllWindows()