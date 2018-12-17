import numpy as np
import cv2
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文标签
def convert(img):
    (r,g,b)=cv2.split(img)
    img=cv2.merge([b,g,r])
    return img

img1 = cv2.imread('pic1.jpg') #查询图像1
img1 = convert(img1)
img2 = cv2.imread('pic2.jpg') #查询图像2
img2 = convert(img2)
sift = cv2.cv2.xfeatures2d.SIFT_create()

#利用sift找到特征和特征的描述
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)


# 比值测试，首先获取与 A 距离最近的点 B（最近）和 C（次近），只有当 B/C
# 小于阈值时（0.75）才被认为是匹配，因为假设匹配是一一对应的，真正的匹配的理想距离为 0
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
#报错，显示第六个参数没有，解决方法，设置为None
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good[:10],None)

plt.subplot(221),plt.imshow(img1),plt.title(u'原始图像1')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(img2),plt.title(u'原始图像2')
plt.xticks([]), plt.yticks([])
plt.subplot(212),plt.imshow(img3),plt.title(u'图像匹配')
plt.xticks([]), plt.yticks([])
plt.show()
