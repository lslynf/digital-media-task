from stitch import Stitcher
import imutils
import cv2
import os

path = "pic"
names = os.listdir(path)

imgs=[]
stitcher = Stitcher()
for i in range(1,len(names)+1):
    name="pic/s"+str(i)+".jpg"
    img = cv2.imread(name)
    img = imutils.resize(img, width=400)
    imgs.append(img)



imga=imgs[0]
# print(imga.shape)
imgb=imgs[1]
# print(imgb.shape)
(result, vis) = stitcher.stitch([imga,imgb], showMatches=True)
# print(result.shape)
cv2.imshow('0',result)
cv2.waitKey(5)
# result=imutils.resize(result,width=400)
# imgc=imgs[2]
# imgc=imutils.resize(imgc,width=400)
# (result,vis1)=stitcher.stitch([result,imgc],showMatches=True)

cnt=0
sum=0
for img in imgs[2:]:
    cnt+=1
    y=580+sum
    result = result[0:224, 0:y]
    win = "" + str(cnt)
    # cv2.imshow(win, result)
    # cv2.waitKey(2)
    img=imutils.resize(img,width=400)
    (result,vis)=stitcher.stitch([result,img],showMatches=True)
    # cv2.imshow(win, result)
    # cv2.waitKey(2)
    sum += 135

cv2.imshow("Result", result)
cv2.waitKey()
