import cv2 as cv
from PIL import Image
from util import get_limits
import os

web_cam = cv.VideoCapture(0)
_image = cv.imread(os.path.join('./Color Detection/', 'road.jpg'))
blue = [0, 255, 255]

def ImageColour_detection(img, color):
    hsv_image = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=color)
    mask = cv.inRange(hsv_image, lowerLimit, upperLimit)
    Image_mask = Image.fromarray(mask)
    bbox = Image_mask.getbbox()
    if bbox is not None:
        x1, y1, w, h = bbox
        cv.rectangle(img, (x1, y1), (w+x1, h+y1), (0, 0, 255), 1)
    
    cv.imshow("Objects", img)
    cv.waitKey(0)

def WebCam_Color_detection(cam, color):
    while True:
        ret, frame = cam.read()
        
        hsv_Image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lowerLimit, upperLimit = get_limits(color=color)
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


ImageColour_detection(img=_image, color=blue)
WebCam_Color_detection(cam=web_cam, color=blue)























