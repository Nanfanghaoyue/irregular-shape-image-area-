import cv2
import numpy as np

img=cv2.imread('sample.png')
#灰度
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#查找轮廓
contours,hierarchy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#绘制轮廓
cv2.drawContours(img,contours,-1,(0,255,0),3)
#绘制轮廓后的图像
cv2.imshow('Contours',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#计算面积
area = 0
for i in contours:
    area += cv2.contourArea(i)
print(area)