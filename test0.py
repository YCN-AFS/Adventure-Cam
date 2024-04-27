import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)
pose = mp_pose.Pose()

while True:
    success, image = cap.read()
    if not success:
        break

    # Convert the image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image
    results = pose.process(image)

    # Get the pose landmarks
    pose_landmarks = results.pose_landmarks

    if pose_landmarks:
        # Get the landmark corresponding to the left knee
        left_knee = pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]

        # Get the x and y coordinates of the left knee
        x = left_knee.x
        y = left_knee.y

        # Get the z coordinate (depth) if available
        z = left_knee.z if left_knee.HasField('z') else None

        # Do something with the left knee coordinates
        print(f"Left Knee: x={x}, y={y}, z={z}")

    # Display the image
    cv2.imshow('Pose Detection', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()