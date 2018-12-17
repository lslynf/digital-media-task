#_*_coding:utf-8_*_
import cv2
import numpy as np

def contrast(x,y):
    row,col,channels=srcim.shape
    for i in range(row):
        for j in range(col):
            for k in range(channels):
                temp=x*srcim[i][j][k]*0.01+y
                if temp>255 :
                    newim[i][j][k]=255
                elif temp<0 :
                    newim[i][j][k]=0
                else:
                    newim[i][j][k]=temp

srcim=cv2.imread('people.jpg')
cv2.imshow('init',srcim)
cv2.waitKey(5)
newim=np.zeros(srcim.shape,np.uint8)
a=100
b=50
contrast(a,b)
cv2.imshow("result", newim)
cv2.waitKey(0)




