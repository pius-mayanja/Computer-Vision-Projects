import cv2
import mediapipe as mp

image = cv2.imread('./hire.png')

mp_face_detection = mp.solutions.face_detection
face_detector = mp_face_detection.FaceDetection(min_detection_confidence=0.5)
results = face_detector.process(image)

if results.detections:
    for detection in results.detections:
        # Get bounding box coordinates
        bboxC = detection.location_data.relative_bounding_box
        h, w, _ = image.shape
        bbox = int(bboxC.xmin * w), int(bboxC.ymin * h), \
               int(bboxC.width * w), int(bboxC.height * h)
        # Draw rectangle around detected face
        cv2.rectangle(image, bbox, (0, 255, 0), 2)

cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
