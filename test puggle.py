import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('puggle.jpg', cv2.IMREAD_COLOR)

scale = 0.2

height = int(img.shape[0]*scale)
width = int(img.shape[1]*scale)
print(height, width)

img = cv2.resize(img, (width, height))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(img, cmap ='gray', interpolation ='bicubic')
#plt.show()

#cam = cv2.VideoCapture(0)

#while True:
#    ret, frame = cam.read()
#    cv2.imshow('poop',frame)