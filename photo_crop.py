import cv2
import sys
import time
# cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)
num_pics = 0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        sub_face = frame[y:y+h, x:x+w]
        file_name = "face_pic_" + str(num_pics) + ".jpg"
        cv2.imwrite(file_name, sub_face)
        num_pics += 1

    # Display the resulting frame
    cv2.imshow('Video', frame)
    time.sleep(1)

    if num_pics >= 8:
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()