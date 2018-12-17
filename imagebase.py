# _*_ coding:utf-8 _*_
import cv2
import numpy
#读取图片
im =cv2.imread('people.jpg')
print(im.shape)
cv2.imshow('init',im)
cv2.waitKey(5)
# 交换B和R
for i in range(0,333):
    for j in range(0,500):
        temp=im[i][j][2]
        im[i][j][2]=im[i][j][0]
        im[i][j][0]=temp
# 图片变成灰度
cv2.imshow('change',im)
cv2.waitKey()
gray_im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
cv2.imshow('changegray',gray_im)
cv2.waitKey(5)

# 变成yuv色彩空间
yuv_im=cv2.cvtColor(im,cv2.COLOR_BGR2YUV)
for i in range(0,333):
    for j in range(0,500):
          yuv_im[i][j][1]=yuv_im[i][j][2]=128
yuv_im=cv2.cvtColor(yuv_im,cv2.COLOR_YUV2BGR)
cv2.imshow('changeyuv',yuv_im)
cv2.waitKey(5)
# 变成hsv空间
hsv_im=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
for i in range(0,333):
    for j in range(0,500):
        hsv_im[i][j][1]=hsv_im[i][j][1]+50
hsv_im=cv2.cvtColor(hsv_im,cv2.COLOR_HSV2BGR)#在进行转换后要进行显示要再转回
cv2.imshow('changehsv',hsv_im)
cv2.waitKey()

