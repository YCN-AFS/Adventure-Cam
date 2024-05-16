import mediapipe as mp
import cv2
#https://youtu.be/06TE_U21FK4?si=luKRS0RghSJ4V6AF&t=1495
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose



cap = cv2.VideoCapture('test.mp4')
cap.set(3, 640)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()


        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        #Make detection
        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        #Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)



        cv2.imshow('FoxCode', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()