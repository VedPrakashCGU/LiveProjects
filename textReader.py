import easyocr
import cv2
import matplotlib.pyplot as plt


image_path='C:/Users/user/Desktop/ImageClassification/Image Dataset/imageReader.jpg'
img=cv2.imread(image_path)

reader=easyocr.Reader(['en'],gpu=False)


text_=reader.readtext(img)

for t in text_:
    bbox,text,score=t
    print(text)
    #print(bbox[0])
    cv2.rectangle(img,(int(bbox[0][0]),int(bbox[0][1])),(int(bbox[2][0]),int(bbox[2][1])),(0,255,0),2)
    cv2.putText(img,text,(int(bbox[0][0]),int(bbox[0][1])),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()