import cv2
import sys
import time
# cascPath = sys.argv[1]
def crop_photo():
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
            flags=cv2.COLOR_BGR2GRAY
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            sub_face = frame[y:y+h, x:x+w]
            file_name = "./new/face_pic_34" + str(num_pics) + "_saul1.jpg"
            sub_face = cv2.resize(sub_face, (273, 273))
            cv2.imwrite(file_name, sub_face)
            num_pics += 1
            time.sleep(.25)
        # Display the resulting frame
        # cv2.imshow('Video', frame)

        if num_pics >= 14:
            break

    # When everything is done, release the capture
    video_capture.release()
    # cv2.destroyAllWindows()
crop_photo()
