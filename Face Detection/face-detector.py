import cv2

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
image = cv2.imread(r'C:\Users\mayan\Desktop\Computer-Vision-Projects\Face Detection\2faces.jpg')

faces = face_detector.detectMultiScale(image, scaleFactor=1.3, minNeighbors=6)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
    
cv2.imshow("FACES", image)
cv2.waitKey(0)

cv2.destroyAllWindows()