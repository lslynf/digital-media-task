# _*_ coding:utf-8 _*_
import cv2
import numpy as np

#计算暗通道
def darkchannel(init):
    minimg = np.zeros(init.shape, np.uint8)
    dark=np.zeros(init.shape,np.uint8)
    row,col,channels = init.shape
    #取rgb最小值
    for i in range(row):
        for j in range(col):
            temp = min(init[i,j,0],init[i,j,1],init[i,j,2])
            minimg[i,j,0] = minimg[i,j,1] = minimg[i,j,2] = temp
    patchsize=4
    size=int(patchsize/2)
    replicate=cv2.copyMakeBorder(minimg,size,size,size,size,cv2.BORDER_REPLICATE)
    #取灰度最小值
    newimg=np.zeros(replicate.shape,np.uint8)
    for i in range(size,row+size):
        for j in range(size,col+size):
                temp = (replicate[i-size:i+size+1,j-size:j+size+1,0]).reshape(1,(patchsize+1)*(patchsize+1))[0].tolist()
                temp.sort()
                newimg[i,j] = [temp[0],temp[0],temp[0]]
    # cv2.imshow('newimg',newimg)
    # cv2.waitKey(2)
    for i in range(row):
        for j in range(col):
            minimg[i,j]=newimg[i+size,j+size]
    cv2.imshow('dark',minimg)
    cv2.waitKey(3)
    return minimg

#计算大气光成分
def getA(darkimg,src):
    row,col,channel = darkimg.shape
    L = []
    size = int(0.001*(row*col))
    for i in range(row):
        for j in range(col):
            pixel = [i,j,darkimg[i,j,0]]
            L.append(pixel)
    L = sorted(L,key=lambda x: x[2],reverse=True)
    #取前0.1%的像素,在原图中找到亮度最大的点作为A值
    firstlist=[]
    for i in range(size):
        firstlist.append(L[i])
    maxA = -1
    for i in range(len(firstlist)):
        x = firstlist[i][0]
        y = firstlist[i][1]
        avg = int((int(src[x,y,0])+int(src[x,y,1])+int(src[x,y,2]))/3)
        maxA = max(maxA,avg)
    return [maxA,maxA,maxA]

#计算投射率t
def getT(darkimg,A):
    tximg = np.zeros(darkimg.shape, np.float)
    row,col,channels = darkimg.shape
    w = 0.95
    for i in range(row):
        for j in range(col):
            for k in range(channels):
                tximg[i,j,k] = 1-w*float(darkimg[i,j,k]*1.0/A[k]*1.0)
    cv2.imshow('tx',tximg)
    cv2.waitKey(2)
    return tximg

#计算去雾之后的图像
def Dehaze(initimg,A,tx):
    resimg = np.zeros(initimg.shape, np.uint8)
    t = 0.1
    row,col,channels = initimg.shape
    for i in range(row):
        for j in range(col):
            for k in range(channels):
                resimg[i,j,k] = int((initimg[i,j,k]-A[k])*1.0/max(t,tx[i,j,k])*1.0)+A[k]
                if resimg[i,j,k]>255:
                    resimg[i,j,k]=255
    return resimg
if __name__ == '__main__':
    initimg=cv2.imread('haze1.png')
    cv2.imshow('init',initimg)
    cv2.waitKey(3)
    darkimg = darkchannel(initimg)
    A = getA(darkimg,initimg)
    tx = getT(darkimg,A)
    res = Dehaze(initimg,A,tx)
    cv2.imshow('res',res)
    cv2.waitKey()