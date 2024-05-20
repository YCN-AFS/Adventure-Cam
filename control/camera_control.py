import mediapipe as mp
import cv2
import numpy as np

#https://youtu.be/06TE_U21FK4?si=luKRS0RghSJ4V6AF&t=1495
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose



cap = cv2.VideoCapture(0)
cap.set(3, 640)



def calculation_angle(a, b, c):
    a = np.array(a) #First
    b = np.array(b) #Mid
    c = np.array(c) #End
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180 / np.pi)
    if angle > 180:
        angle = 360 - angle
    return angle



with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=2) as pose:
    while cap.isOpened():
        ret, frame = cap.read()


        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        #Make detection
        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark
            print(landmarks)
        except:
            print("Pass")
            pass

        #Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)



        cv2.imshow('FoxCode', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()