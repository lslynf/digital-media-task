import cv2
im=cv2.imread('bicycle.jpg')
cv2.imshow('init',im)
cv2.waitKey(5)
row,col,channel=im.shape
increment=50
increment=increment/100
for i in range(row):
    for j in range(col):
        rgbmax=max(im[i][j][0],im[i][j][1],im[i][j][2])
        rgbmin=min(im[i][j][0],im[i][j][1],im[i][j][2])
        delta=(int(rgbmax)-int(rgbmin))/255
        if delta==0:
            continue
        value=(int(rgbmax)+int(rgbmin))/255*1.0
        l=value/2
        if l<0.5:
            s=delta/value
        else:
            if 2-value==0:
                s=10
            else:
                s=delta/(2-value)
        if increment>0:
            if increment+s>=1:
                alpha=s
            else:
                alpha=1-increment
            alpha=1/alpha-1;
            im[i][j][0]=im[i][j][0]+(im[i][j][0]-l*255)*alpha
            im[i][j][1] = im[i][j][1] + (im[i][j][1] - l * 255) * alpha
            im[i][j][2] = im[i][j][2] + (im[i][j][2] - l * 255) * alpha
        else:
            alpha=increment
            im[i][j][0]=l*255+(im[i][j][0]-l*255)*(1+alpha)
            im[i][j][1] = l * 255 + (im[i][j][1] - l * 255) * (1 + alpha)
            im[i][j][2] = l * 255 + (im[i][j][2] - l * 255) * (1 + alpha)
cv2.imshow('result',im)
# cv2.namedWindow('result')
# cv2.createTrackbar('size','result',scale,4,contrast)
cv2.waitKey(0)