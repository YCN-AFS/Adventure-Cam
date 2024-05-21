import mediapipe as mp
import cv2
import numpy as np

#https://youtu.be/06TE_U21FK4?si=luKRS0RghSJ4V6AF&t=1495
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose






def running_workouts():
    pass

def put_text_on_image(image):
    pass

def calculation_angle(a, b, c):
    a = np.array(a) #First
    b = np.array(b) #Mid
    c = np.array(c) #End
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180 / np.pi)
    if angle > 180:
        angle = 360 - angle
    return angle

cap = cv2.VideoCapture(0)
#Curl counter varibles
counter = 0
stage = None
cap.set(3, 640)
ret, frame = cap.read()
width, height = frame.shape[0], frame.shape[1]

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

            #Get coordinates
            left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

            #Calculation angle
            angle = calculation_angle(left_hip, left_shoulder, left_elbow)
            #Visulize angle
            cv2.putText(image, str(round(angle, 2)), tuple(np.multiply(left_shoulder, (height, width)).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            #Curl counter logic
            if angle > 150:
                stage = "Down"
            if angle < 30 and stage == "Down":
                stage = "Up"
                counter += 1

            cv2.putText(image, str(counter), (100, 100), cv2.FONT_HERSHEY_SIMPLEX,2, (255, 255, 255), 2, cv2.LINE_AA)

        except:
            pass

        #Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.imshow('FoxCode', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()