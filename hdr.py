import cv2
import numpy as np
from matplotlib import pyplot as plt


def readImagesAndTimes():
  
  times = np.array([ 1/30.0, 0.25, 2.5, 15.0 ], dtype=np.float32)
  
  filenames = ["img_0.033.jpg", "img_0.25.jpg", "img_2.5.jpg", "img_15.jpg"]

  images = []
  for filename in filenames:
    im = cv2.imread(filename)
    images.append(im)
  
  return images, times

if __name__ == '__main__':
  # 获取图片
  images, times = readImagesAndTimes()
  
  
  # 图像对齐，图像未对准会导致严重的结果
  alignMTB = cv2.createAlignMTB()
  alignMTB.process(images, images)
  
  # 获取相机的函数
  calibrateDebevec = cv2.createCalibrateDebevec()
  responseDebevec = calibrateDebevec.process(images, times)
  
  # 合成原始图片
  mergeDebevec = cv2.createMergeDebevec()
  hdrDebevec = mergeDebevec.process(images, times, responseDebevec)
  cv2.imwrite("hdrDebevec.hdr", hdrDebevec)

  
  # 色调映射
  tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
  ldrDrago = tonemapDrago.process(hdrDebevec)
  ldrDrago = 3 * ldrDrago
  cv2.imwrite("ldr-Drago.jpg", ldrDrago * 255)

  img1=cv2.imread('img_0.033.jpg')
  (r, g, b)=cv2.split(img1)
  img1=cv2.merge([b,g,r])

  img2 = cv2.imread('img_0.25.jpg')
  (r, g, b) = cv2.split(img2)
  img2 = cv2.merge([b, g, r])

  img3 = cv2.imread('img_2.5.jpg')
  (r, g, b) = cv2.split(img1)
  img3 = cv2.merge([b, g, r])

  img4 = cv2.imread('img_15.jpg')
  (r, g, b) = cv2.split(img4)
  img4 = cv2.merge([b, g, r])

  img5 = cv2.imread('ldr-Drago.jpg')
  (r, g, b) = cv2.split(img5)
  img5 = cv2.merge([b, g, r])

  plt.subplot(241), plt.imshow(img1)
  plt.xticks([]), plt.yticks([])
  plt.subplot(242), plt.imshow(img2)
  plt.xticks([]), plt.yticks([])
  plt.subplot(243), plt.imshow(img3)
  plt.xticks([]), plt.yticks([])
  plt.subplot(244), plt.imshow(img4)
  plt.xticks([]), plt.yticks([])
  plt.subplot(212), plt.imshow(img5)
  plt.xticks([]), plt.yticks([])
  plt.show()
