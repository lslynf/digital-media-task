import cv2
import numpy as np


#转灰度图计算得到能量图，利用sobel算子
def gete(grayimg):
    imgx=cv2.Sobel(grayimg,-1,1,0,ksize=3)
    imgy=cv2.Sobel(grayimg,-1,0,1,ksize=3)
    eimg=imgx+imgy
    # cv2.imshow('e',eimg)
    # cv2.waitKey(3)
    # print("能量图")
    # print(eimg)
    return eimg

#dfs删除路径
def deletepath(init,newimg,path,x,y):
    if x<0 or y<0:
        return init
    # print(init)
    row,col=newimg.shape
    for j in range(y,col-1):
        init[x,j]=init[x,j+1]
    if path[x,y]==0:
        deletepath(init,newimg,path,x-1,y-1)
    elif path[x,y]==1:
        deletepath(init,newimg,path,x-1,y)
    elif path[x,y]==2:
        deletepath(init,newimg,path,x-1,y+1)

#找到一条最小路径并删除
def getpath(grayimg,eimg1,cnt):
    row,col=eimg1.shape
    neweimg=np.zeros(eimg1.shape,int)
    for i in range(0,row):
        for j in range(0,col):
            neweimg[i,j]=eimg1[i,j]
    path=np.zeros(eimg1.shape, np.uint8)#记录来的方向
    for i in range(1,row):
        for j in range(0,col):
            if j==0:
                temp=min(neweimg[i-1,j],neweimg[i-1,j+1])
                if temp == neweimg[i - 1, j]:
                    path[i][j] = 1
                elif temp == neweimg[i - 1, j + 1]:
                    path[i][j] = 2
            elif j==col-1:
                temp=min(neweimg[i-1,j-1],neweimg[i-1,j])
                if temp==neweimg[i-1,j-1]:
                   path[i][j]=0
                elif temp==neweimg[i-1,j]:
                   path[i][j]=1
            else:
                temp=min(neweimg[i-1,j-1],neweimg[i-1,j],neweimg[i-1,j+1])
                if temp==neweimg[i-1,j-1]:
                   path[i][j]=0
                elif temp==neweimg[i-1,j]:
                   path[i][j]=1
                elif temp==neweimg[i-1,j+1]:
                   path[i][j]=2
            neweimg[i,j]=neweimg[i,j]+temp
    # for j in range(0,col):
    #     print(neweimg[row-1][j],end=" ")
    # print('\n')

    #找到最小的位置
    minvalue=1e9
    minid=0
    for j in range(0,col):
        if neweimg[row-1,j]<minvalue:
            minvalue=neweimg[row-1,j]
            minid=j
    # print(minid)
    deletepath(grayimg,neweimg,path,row-1,minid)
    m,n=grayimg.shape
    resimg=np.zeros([m,n-cnt+1],np.uint8)
    r,c=resimg.shape
    for i in range(0,r):
        for j in range(0,c):
            resimg[i,j]=grayimg[i,j]
    # print('新图')
    # print(resimg)
    return resimg

def SeamCarving(grayimg,nums):
    row, col = grayimg.shape
    initimg = np.zeros(grayimg.shape, np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            initimg[i, j] = grayimg[i, j]
    for i in range(0,nums):
        eimg=gete(initimg)
        resimg=getpath(initimg,eimg,i+1)
        r,c=resimg.shape
        for i in range(0,r):
            for j in range(0,c):
                initimg[i,j]=resimg[i,j]
    scaleImg=np.zeros([row,col-nums],np.uint8)
    for i in range(row):
        for j in range(col-nums):
            scaleImg[i,j]=initimg[i,j]
    return scaleImg

if __name__=='__main__':
    img = cv2.imread('width.jpg')
    print(img.shape)
    cv2.imshow('init', img)
    cv2.waitKey(5)
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print('原始')
    # print(grayimg)
    resimg=SeamCarving(grayimg,100)
    cv2.imshow('result',resimg)
    cv2.waitKey()
