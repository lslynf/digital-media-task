# _*_ coding:utf-8 _*_
import cv2
from matplotlib import pyplot as plt
#注：在opencv中是用bgr表示，而matplotlib是用rgb表示
plt.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False  #用来正常显示负号
img = cv2.imread('star.jpg')
(r, g, b)=cv2.split(img)
img=cv2.merge([b,g,r])

#均值滤波
res1 = cv2.blur(img,(5,5))

#高斯滤波
res2=cv2.GaussianBlur(img,(5,5),0)

#中值滤波
res3=cv2.medianBlur(img,5)

#双边滤波
res4=cv2.bilateralFilter(img,9,75,75)

plt.subplot(321),plt.imshow(img),plt.title(u'原始图像')
plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(res1),plt.title(u'均值滤波')
plt.xticks([]), plt.yticks([])
plt.subplot(323),plt.imshow(res2),plt.title(u'高斯滤波')
plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.imshow(res3),plt.title(u'中值滤波')
plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.imshow(res4),plt.title(u'双边滤波')
plt.xticks([]), plt.yticks([])
plt.show()
