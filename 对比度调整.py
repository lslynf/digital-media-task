#_*_coding:utf-8_*_
import cv2
import numpy as np
def contrast(a):
    a = cv2.getTrackbarPos('size', 'result')
    a=a/50
    row,col,channels=srcim.shape
    newim = np.zeros(srcim.shape,np.uint8)
    for i in range(row):
        for j in range(col):
            for k in range(channels):
                temp=srcim[i,j,k]-L[k]
                temp*=a
                temp+=L[k]
                if temp>255:
                    newim[i,j,k]=255
                elif temp<0:
                    newim[i,j,k]=0
                else:
                    newim[i,j,k]=int(temp)
    cv2.imshow("result", newim)


srcim=cv2.imread('bicycle.jpg')
srcim1 = np.zeros(srcim.shape,np.uint8)
avgb,avgg,avgr=0,0,0
x,y,z=srcim.shape
for i in range(x):
    for j in range(y):
        avgb=avgb+srcim[i,j,0]
        avgg=avgg+srcim[i,j,1]
        avgr=avgr+srcim[i,j,2]
psum=srcim.shape[0]*srcim.shape[1]
avgb,avgg,avgr=int(avgb/psum),int(avgg/psum),int(avgr/psum)
L=[avgb,avgg,avgr]

cv2.namedWindow('result')
cv2.imshow('result',srcim)
cv2.createTrackbar('size','result',50,100,contrast)
cv2.waitKey(0)




