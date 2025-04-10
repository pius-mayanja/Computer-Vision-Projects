import cv2

plate1 = cv2.imread(r'C:\Users\mayan\Desktop\Computer-Vision-Projects\Number Plate Detection\plate1.jpg')
plate2 = cv2.imread(r'C:\Users\mayan\Desktop\Computer-Vision-Projects\Number Plate Detection\plate2.jpg')
plate3 = cv2.imread(r'C:\Users\mayan\Desktop\Computer-Vision-Projects\Number Plate Detection\plate3.jpg')

resized = cv2.resize(plate1,(2000,1000))

number_plate_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')
plates = number_plate_detector.detectMultiScale(resized, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in plates:
    cv2.rectangle(resized, (x,y), (x+w,y+h), (0,0,255), 6)

cv2.imshow("Plate", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()