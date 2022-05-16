# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import matplotlib.pyplot as plt

# initialize the camera and grab a reference to the raw camera capture
#camera = PiCamera()
#rawCapture = PiRGBArray(camera)
# allow the camera to warmup
#time.sleep(0.1)
# grab an image from the camera
#camera.capture(rawCapture, format = 'rgb')
#image = rawCapture.array
#image =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Initialize the camera
camera = PiCamera()
 
# Set the camera resolution
camera.resolution = (640, 480)
 
# Set the number of frames per second
camera.framerate = 32

camera.rotation = 180
 
# Generates a 3D RGB array and stores it in rawCapture
raw_capture = PiRGBArray(camera, size=(640, 480))
 
# Wait a certain number of seconds to allow the camera time to warmup
time.sleep(0.1)
 
# Capture frames continuously from the camera
for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
     
    # Grab the raw NumPy array representing the image
    image = frame.array
    
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    retval, threshold =  cv2.threshold(image, 70, 255, cv2.THRESH_BINARY)
    
    th = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    #cv2.line(image, (0,10), (150, 150), (0,0,255), 15)
    # Display the frame using OpenCV
    cv2.imshow("original", image)
    cv2.imshow("Threshold", threshold)
    cv2.imshow("Gaussian", th)

     
    # Wait for keyPress for 1 millisecond
    key = cv2.waitKey(1)
     
    # Clear the stream in preparation for the next frame
    raw_capture.truncate(0)
    #cv2.destroyAllWindows()
    #break
     
    # If the `q` key was pressed, break from the loop
    if key == ord("q"):
        cv2.destroyAllWindows()
        break


#cv2.line(image, (0,0), (150, 150),(0,0,255),15)
# display the image on screen and wait for a keypress

#plt.imshow(image, cmap ='gray', interpolation ='bicubic')
#plt.show()


#cv2.imshow("Image", image)

#cv2.waitKey(0)

#cv2.destroyAllWindows()