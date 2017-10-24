"""Determine if there is car in bike lane with openCV.
"""


import numpy as np
import cv2
import requests
#from tweet import tweet

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

face_cascade = cv2.CascadeClassifier('cars.xml')#best
#face_cascade = cv2.CascadeClassifier('cas4.xml')
# face_cascade = cv2.CascadeClassifier('cars.xml')
# face_cascade = cv2.CascadeClassifier('cars.xml')
# face_cascade = cv2.CascadeClassifier('cars.xml')
# face_cascade = cv2.CascadeClassifier('cars.xml')


cap = cv2.VideoCapture('vid.mp4')
informed = False

while 1:
    try:
        ret, img = cap.read()
#         print (img.shape)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,minNeighbors =20)#, minNeighbors =40 ,scaleFactor=1.1)#,3, 3)#, 1.3, 5)

        for (x,y,w,h) in faces:
            mid_in = (x + x+ w)/2
            right_th = 390
            left_th = 300

            if left_th <= mid_in <= right_th:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                print ("there is car in bike lane")
                if not informed:
                    requests.post("http://bike-thing-server.herokuapp.com/hazard")
                    informed = True
                    #tweet("@TOPolice There is a flying car with license plate SXP 344 on Yonge Street")

            if mid_in <= left_th:
                pass
                #print ("there is car to the left of bike lane")

            if right_th  <= mid_in:
                pass
                #print ("there is car to the right of lane")

        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff

    except:
        break

    if k == 27: #pressing escape
        break

cap.release()
cv2.destroyAllWindows()
