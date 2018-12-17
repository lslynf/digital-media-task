# _*_ coding:utf-8 _*_
import cv2
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文标签

img=cv2.imread('woman.jpg')
(r, g, b)=cv2.split(img)
img=cv2.merge([b,g,r])

res=cv2.GaussianBlur(img,(3,3),0)

newimg=np.zeros(img.shape,np.uint8)

def kenel(ux,uy,x,y,sigma):
    e = 2.718281828459
    pi = 3.1415926
    vx = (x-ux)*(x-ux)/(2*(sigma*sigma))
    vy = (y-uy)*(y-uy)/(2*(sigma*sigma))
    return (e**(-vx-vy))/(2*pi*sigma*sigma)
def Gaussfilter(img,newimg,a,sigma):
    M = a*a
    row, col, ch = img.shape
    da = a//2
    for i in range(0, row ):
        for j in range(0 , col):
            for k in range(3):
                sum = 0
                for x in range(M):
                    di = i - da + int(x // a)
                    dj = j - da + int(x % a)
                    if(di<=0):di = 0
                    if(di>=row):di = row-1
                    if(dj<=0):dj = 0
                    if(dj>=col):dj = col-1
                    sum += img[di, dj, k] * kenel(i,j,di,dj,sigma)
                newimg[i, j, k] = sum
row,col,ch=img.shape
newimg = np.zeros([row, col, ch], img.dtype)
Gaussfilter(img,newimg,5,1.5)
plt.subplot(131),plt.imshow(img),plt.title(u'原始图像')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(res),plt.title(u'opencv高斯滤波')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(newimg),plt.title(u'实现高斯滤波')
plt.xticks([]), plt.yticks([])
plt.show()

