import cv2
import sys

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")
video_capture = cv2.VideoCapture(0)

while True:

    #capture frame by frame
    retval,frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray ,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(35,35)
    )

    #draw a rectangle around recognized faces
    for(x, y, w , h ) in faces:
         cv2.rectangle (frame,( x, y),(x+w, y+w),(50,50,200),2)
            #display the result frame

    cv2.imshow('video',frame)

    #exit the camera view

   # Exit the camera view
    if cv2.waitKey(1) & 0xFF == ord('q'):
       sys.exit()
