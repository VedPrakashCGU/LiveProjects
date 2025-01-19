#read the image
#detect the co-ordinate of the image
#blur the image on the co-ordinate 
#Show the image
import cv2
faceCascade=cv2.CascadeClassifier("c://users//user//anaconda3//Lib//site-packages//cv2//data//haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if not ret:
        print("the frame is not captured")
        break
    # converting the image from bgr into grayscale
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=faceCascade.detectMultiScale(gray_img,scaleFactor=5)
    for x,y,w,h in face:
        face_roi=frame[y:y+h,x:x+w]
        blurd_face=cv2.GaussianBlur(face_roi,(99,99),30)
        
        frame[y:y+h,x:x+w]=blurd_face
    cv2.imshow("Face anonylzer",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 




