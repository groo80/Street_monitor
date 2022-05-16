# Traffic Monitor camera
Build of a camera monitor to track cars, bikes, skateboard, scooters, animals and pedestrians on the street.
Point: to capture traffice passing in front of the house.

Purpose: learn how to start object detection on pi on my own. 


Step 1: install hardware: Done (raspberry pi 4 + camera)
Step 2: install openCV
Following these steps for openCV- https://qengineering.eu/install-opencv-4.5-on-raspberry-pi-4.html
** Finally top one, previous 2 were tried but seem old.
https://littlebirdelectronics.com.au/guides/165/set-up-opencv-on-raspberry-pi-4
note - lib___dev12 not found. Check, if not working investigate
YOLO
https://medium.datadriveninvestor.com/object-detection-with-raspberry-pi-and-python-bc6b3a1d4972

Plan: 
1 - Yolo - detect objects
2 - Make bounding boxes and measure at fixed intervals to find the movement across the screen

Difficulty 
- neigbhors park cars across the street
- window tilt...

Output image:
1 file with detection object (colour of object?) + a few position measurements + datetime
2 metrics of detected objects that I can play with (frequency of foxes in street at what time, etc)
3 calculate speed of the objects
4 Direction of movement
5 save small photo samples


