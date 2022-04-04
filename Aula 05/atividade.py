# coding=utf-8
import cv2
import numpy as np

imagem = cv2.imread('../logo-if.jpg')

#ajusta brilho
def ajuste_brilho(img,br):
    brilho=[br,br,br]
    res=np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            #soma valor do pixel + intensidade do brilho
            res[y, x] = np.minimum(img[y,x]+brilho,[255,255,255])
    return res

def contrast(img, alfa):
    #initilize a empty matrix
    res=np.zeros(img.shape, np.uint8)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            res[y,x] = np.minimum(img[y,x]*alfa,[255,255,255])
    return res

def negative(img):
    res = cv2.bitwise_not(img)
    return res

cv2.namedWindow('Brilho')
brilho=0
result=imagem

while(True):
    cv2.imshow('Brilho',result)
    k=cv2.waitKey(20)
    if k == 27:
        break
    elif k == ord('a'):
        brilho=min(brilho+50,255)
        result=ajuste_brilho(imagem,brilho)
    elif k == ord('z'):
        brilho=max(brilho-50,0)
        result=ajuste_brilho(imagem,brilho)
    elif k == ord('s'):
        brilho=min(brilho - 0.1, 3.0)
        result=contrast(imagem, brilho)
    elif k == ord('x'):
        brilho=max(brilho + 0.1, 0)
        result=contrast(imagem, brilho)
    elif k == ord('n'):
        result=negative(imagem)

cv2.destroyAllWindows()