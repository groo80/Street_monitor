# Traffic Monitor camera
Build of a camera monitor to track cars, bikes, skateboard, scooters, animals and pedestrians on the street.
Point: to capture traffice passing in front of the house.

Purpose: learn how to start object detection on pi on my own. 


Step 1: install hardware: Done (raspberry pi 4 + camera)
Step 2: install openCV
Following these steps - https://www.jeremymorgan.com/tutorials/raspberry-pi/how-to-install-opencv-raspberry-pi/
Step 3: 


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


