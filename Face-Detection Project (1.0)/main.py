"""
    This is a simple face recognition project which used Haar-Cascade method
    This project uses the haarcascade_frontal face xml from the cv2 data library
    to detect the face features and alignments

 """

# importing the necessary library

import cv2


# setting up the camera
cam = cv2.VideoCapture(0)

# setting up the path to the xml file

har_cascade = './cascade_container/haarcascade_frontalface_default.xml'

# processing the haarcascade file

face_cascade = cv2.CascadeClassifier(har_cascade)

# frame iterator

while True:

    # reading the camera frames

    success, frame = cam.read()

    # if not success break the loop

    if not success:
        print("ERROR! : couldn't process the frame")
        break

    # color space conversion

    binary_channel_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # processing the binary image to find the face features

    face = face_cascade.detectMultiScale(binary_channel_image, 1.3, 5)

    # getting the number of bounding boxes made

    Faces_detected = len(face)

    # drawing the bounding box

    for x, y, w, h in face:
        # drawing the bounding box around the face

        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # code to count the number of face detected in the frame

    Text = f"Detected Face Count : {Faces_detected} "  # text which is to be displayed on the screen
    Text_position = (20, 50)
    Font_face = cv2.FONT_HERSHEY_SIMPLEX
    Font_scale = 1
    Text_color = (0, 0, 255)
    Text_Thickness = 2
    Text_line_type = cv2.LINE_AA

    frame = cv2.putText(frame, Text, Text_position, Font_face, Font_scale, Text_color, Text_Thickness, Text_line_type)

    cv2.imshow('Face_Detector', frame)

    # stop function

    if cv2.waitKey(20) & 0xFF == ord('c'):
        print("Exited")
        break

# release the resources and destroy the window

cam.release()
cv2.destroyAllWindows()
