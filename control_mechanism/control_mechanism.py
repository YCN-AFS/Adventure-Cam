import mediapipe as mp
import cv2
import numpy as np
#https://youtu.be/06TE_U21FK4?si=G08jxsWFyrLrYwOK&t=2842
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose






def angle_calculation(a, b, c):
    a = np.array(a) #First
    b = np.array(b) #Mid
    c = np.array(c) #End

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180/np.pi)

    if angle > 180:
        angle = 360 - angle
    return angle

cap = cv2.VideoCapture("test.mp4")
cap.set(3, 640)

#Get # Get video width and height
_, frame = cap.read()
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
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

            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

            ange = angle_calculation(shoulder, elbow, wrist)

            #Visualize angle
            cv2.putText(image, str(ange), tuple(np.multiply(elbow, [frame_width, frame_height]).astype(int)),
                                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            # print(mp_pose.PoseLandmark.LEFT_SHOULDER[11][0])
            # print(landmarks[1])
        except:
            pass

        #Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)




        cv2.imshow('FoxCode', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()