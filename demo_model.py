import cv2
import mediapipe as mp
import pickle
import pandas as pd
import numpy as np

# https://youtu.be/We1uB79Ci-w?si=MvKdFtHpr-NRcPgn&t=4171

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose


with open('new_body_language.pkl', 'rb') as file:
    model = pickle.load(file)


cap = cv2.VideoCapture(r"C:\Users\foxcode\Downloads\tai.mp4")
cap.set(3, 640)
ret, frame = cap.read()
width, height = frame.shape[0], frame.shape[1]

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

size = (frame_width, frame_height)

# Below VideoWriter object will create
# a frame of above defined The output
# is stored in 'filename.avi' file.
out = cv2.VideoWriter('tai.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         24, size)

with mp_pose.Pose(min_detection_confidence=0.2, min_tracking_confidence=0.5, model_complexity=1) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Export coordinates
        try:
            body_pose = results.pose_landmarks.landmark
            num_coords = len(body_pose)

            # mark = ['class']
            # for val in range(1, num_coords+1):
            #     mark += ['x{}'.format(val), 'y{}'.format(val), 'z{}'.format(val), 'v{}'.format(val)]





            # extract pose landmarks
            pose_row = list(np.array([[landmarks.x, landmarks.y, landmarks.z, landmarks.visibility] for landmarks in body_pose]).flatten())

            # pose_row.insert(0, class_name)


            # Create file csv
            # if first_time:
            #     with open('cords.csv', 'w', newline='') as csvfile:
            #         writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #         writer.writerow(mark)
            #     first_time = False
            # else:
            #     with open('cords.csv', 'a', newline='') as csvfile:
            #         writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #         writer.writerow(pose_row)

            #Make decisions
            x = pd.DataFrame([pose_row])
            body_language_class = model.predict(x)[0]
            body_language_prob = model.predict_proba(x)[0]
            # print(body_language_class, body_language_prob)


        except:
            pass

        #Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        # Ghi frame video vào tệp tin

        out.write(image)

        # cv2.imshow('FoxCode', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

out.release()

cap.release()
cv2.destroyAllWindows()