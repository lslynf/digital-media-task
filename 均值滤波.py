# _*_ coding:utf-8 _*_
import cv2
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文标签

img=cv2.imread('woman.jpg')
(r, g, b)=cv2.split(img)
img=cv2.merge([b,g,r])

#均值滤波
res = cv2.blur(img,(3,3))

newimg=np.zeros(img.shape,np.uint8)

row,col,channel=img.shape

for i in range(row):
    for j in range(col):
        if i-1>=0 and j-1>=0 and i+1<row and j+1<col:
            temp1=int(img[i - 1, j - 1, 0]) + int(img[i - 1, j, 0]) + int(img[i - 1, j + 1, 0]) + int(img[i, j - 1, 0])+ int(img[i, j, 0]) + int(img[i, j + 1, 0]) + int(img[i + 1, j - 1, 0]) + int(img[i + 1, j, 0]) + int(img[
                 i + 1, j + 1, 0])
            newimg[i, j, 0] = int(temp1 / 9)

            temp2=int(img[i - 1, j - 1, 1]) + int(img[i - 1, j, 1]) + int(img[i - 1, j + 1, 1]) + int(img[i, j - 1, 1])+ int(img[i, j, 1]) + int(img[i, j + 1, 1]) + int(img[i + 1, j - 1, 1]) + int(img[i + 1, j, 1]) + int(img[
                  i + 1, j + 1, 1])
            newimg[i, j, 1] = int(temp2/ 9)

            temp3=int(img[i - 1, j - 1, 2]) + int(img[i - 1, j, 2]) + int(img[i - 1, j + 1, 2]) + int(img[i, j - 1, 2])+ int(img[i, j, 2]) + int(img[i, j + 1, 2]) + int(img[i + 1, j - 1, 2]) + int(img[i + 1, j, 2]) + int(img[
                 i + 1, j + 1, 2])
            newimg[i, j, 2] = int(temp3 / 9)
        else:
            newimg[i, j, 0] = img[i, j, 0]
            newimg[i, j, 1] = img[i, j, 1]
            newimg[i, j, 2] = img[i, j, 2]

plt.subplot(131),plt.imshow(img),plt.title(u'原始图像')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(res),plt.title(u'opencv均值滤波')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(newimg),plt.title(u'实现均值滤波')
plt.xticks([]), plt.yticks([])
plt.show()