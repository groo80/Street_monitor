# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import matplotlib.pyplot as plt

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
# allow the camera to warmup
time.sleep(0.1)
# grab an image from the camera
camera.capture(rawCapture, format = 'bgr', use_video_port = True)
image = rawCapture.array


# Initialize the camera
#camera = PiCamera()
 
# Set the camera resolution
#camera.resolution = (640, 480)
 



#cv2.line(image, (0,0), (150, 150),(0,0,255),15)
# display the image on screen and wait for a keypress

#plt.imshow(image, cmap ='gray', interpolation ='bicubic')
#plt.show()


cv2.imshow("Image", image)

cv2.waitKey(0)

cv2.destroyAllWindows()