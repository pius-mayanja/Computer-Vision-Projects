import cv2 as cv
from PIL import Image
from util import get_limits

cam = cv.VideoCapture(0)

blue = [255, 255, 0]



while True:
    ret, frame = cam.read()
    
    hsv_Image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=blue)
    mask = cv.inRange(hsv_Image, lowerLimit, upperLimit)
    
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)
    
    cv.imshow("WebCam", frame)
    
    if cv.waitKey(1) & 0XFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()

