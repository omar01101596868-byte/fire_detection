import cv2
from pygame import mixer
mixer.init()
sound=mixer.Sound('sound1.mp3')
fire_cascade=cv2.CascadeClassifier("fire_detection_model.xml")
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fire=fire_cascade.detectMultiScale(frame,1.2,5)
    for(x,y,w,h) in fire:
        r_gray=gray[y:y+h,x:x+w]
        r_frame=frame[y:y+h,x:x+w]
        print("fire_detected")
        sound.play()
    cv2.imshow('Video', frame)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break