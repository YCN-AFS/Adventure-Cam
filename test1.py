import cv2
import mediapipe
import math
count = 0

r = 0
theta = 0
setp = []
points = []

drawingModule = mediapipe.solutions.drawing_utils
poseModule = mediapipe.solutions.pose
pose = poseModule.Pose(
    static_image_mode=False,
    min_detection_confidence=0.5)

cap = cv2.VideoCapture(0)
cap.set(3, 1200)  # 3 for width
cap.set(4, 900)  # 4 for height
cap.set(10, 100)  # 10 for brightness

# with poseModule: #(mode=False, upBody=False, smooth=True, detectionCon=0.5):
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Read failure!")
        break

    frame = cv2.flip(frame, 1)

    results = pose.process(frame)
    image_height, image_width, _ = frame.shape

    if results.pose_landmarks:

        drawingModule.draw_landmarks(frame, results.pose_landmarks, poseModule.POSE_CONNECTIONS)
        for ids, lm in enumerate(results.pose_landmarks.landmark):
            cx, cy = lm.x * image_width, lm.y * image_height

            setp.append([cx, cy])

        abx = setp[14][0] - setp[12][0]
        aby = setp[14][1] - setp[12][1]
        acx = setp[24][0] - setp[12][0]
        acy = setp[24][1] - setp[12][1]

        cv2.putText(frame, f"X: {round(setp[18][0], 2)}, Y: {round(setp[18][1], 2)} ", (20, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)

        theta = math.acos((abx*acx + aby*acy)/((math.sqrt(abx**2 + aby**2))*(math.sqrt(acx**2 + acy**2))))


    if theta < math.pi/4:
        theta1 = theta
    if theta > 3*math.pi/4:
        if theta1 < math.pi/4:
            count = count + 1
            theta1 = theta



    # TO RESET THE COUNTER
    if bool(setp):
        r = math.sqrt((setp[12][0] - setp[19][0]) ** 2 + (setp[12][1] - setp[19][1]) ** 2)
    if r < 20:
        count = 0

    cv2.putText(frame, str(count), (150, 250), cv2.FONT_HERSHEY_COMPLEX, 4, (0, 255, 0), 4)

    setp.clear()

    cv2.imshow('FoxCode', frame)


    if cv2.waitKey(1) == ord('q'):  # ESC key
        break


cap.release()
cv2.destroyAllWindows()