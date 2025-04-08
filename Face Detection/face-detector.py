import cv2

images = cv2.imread(r"C:\Users\mayan\Desktop\Computer-Vision-Projects\Face Detection\2faces.jpg")
cam = cv2.VideoCapture(0)

def face_detector_Images(image):
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_detector.detectMultiScale(image, scaleFactor=1.3, minNeighbors=6)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)
        
    cv2.imshow("Detected Faces", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


def face_detector_WebCam(web_cam):
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    while True:
        retrived, frame = web_cam.read()
    
        faces = face_detector.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=8)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            
            
        cv2.imshow("Detected a Face", frame)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
        
    web_cam.release()
    cv2.destroyAllWindows()


print(face_detector_WebCam(web_cam=cam))
print(face_detector_Images(image=images))
            
    
    
    