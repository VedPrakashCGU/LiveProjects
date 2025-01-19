import cv2
face=cv2.CascadeClassifier("C://Users//LENOVO//AppData//Local//Programs//Python//Python312//Lib//site-packages//cv2//data//haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while 1:
    ret,frame=cap.read()
    if not ret:
        print("The camera is not able to open")
        break
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    facedetect=face.detectMultiScale(gray_img,1.1,4)
    for (x,y,w,h) in facedetect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
    cv2.imshow("Camera",frame)
    if cv2.waitKey(10)==ord("a"):
        break
cap.release()