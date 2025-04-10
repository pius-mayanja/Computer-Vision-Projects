import cv2

images = cv2.imread(r"C:\Users\mayan\Desktop\Computer-Vision-Projects\Face Detection\2faces.jpg")
cam = cv2.VideoCapture(0)
vid = cv2.VideoCapture(r"C:\Users\mayan\Desktop\Computer-Vision-Projects\Face Detection\live.mp4")

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
    
        faces, rejects = face_detector.detectMultiScale2(frame, scaleFactor=1.3, minNeighbors=6)


        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            
            
        cv2.imshow("Detected a Face", frame)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
        
    web_cam.release()
    cv2.destroyAllWindows()

def face_detector_Video(video):
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = video.read()
        if not ret:
            break  

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  

        faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("Video Faces", frame)
        if cv2.waitKey(int(1000 / video.get(cv2.CAP_PROP_FPS))) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()

        


print(face_detector_WebCam(web_cam=cam))
print(face_detector_Images(image=images))
print(face_detector_Video(video=vid))
    
    