import mediapipe as mp
import cv2
import math
import numpy as np

#https://youtu.be/06TE_U21FK4?si=luKRS0RghSJ4V6AF&t=1495


def calculation_angle(a, b, c):
    a = np.array(a) #First
    b = np.array(b) #Mid
    c = np.array(c) #End
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180 / np.pi)
    if angle > 180:
        angle = 360 - angle
    return angle



class ReceiveAction:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.counter = 0
        self.stage = None
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.cap.set(3, 640)
        _, self.frame = self.cap.read()
        self.width, self.height = self.frame.shape[0], self.frame.shape[1]

    def get_angle(self, landmark1, landmark2, landmark3):
        """
        Returns the angle (in radians) between three landmarks.
        """
        x1, y1 = landmark1
        x2, y2 = landmark2
        x3, y3 = landmark3

        vector1 = (x1 - x2, y1 - y2)
        vector2 = (x3 - x2, y3 - y2)

        dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
        magnitudes = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2) * math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)

        if magnitudes == 0:
            return 0

        angle = dot_product / magnitudes
        angle = math.acos(angle)

        return angle

    def player_direction_view(self, results, image):
        self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

        left_eye = results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.LEFT_EYE]
        right_eye = results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.RIGHT_EYE]
        nose_tip = results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.NOSE]

        left_eye_x, left_eye_y = int(left_eye.x * image.shape[1]), int(left_eye.y * image.shape[0])
        right_eye_x, right_eye_y = int(right_eye.x * image.shape[1]), int(right_eye.y * image.shape[0])
        nose_tip_x, nose_tip_y = int(nose_tip.x * image.shape[1]), int(nose_tip.y * image.shape[0])
        left_eye_angle = self.get_angle((nose_tip_x, nose_tip_y), (left_eye_x, left_eye_y), (right_eye_x, right_eye_y))
        right_eye_angle = self.get_angle((nose_tip_x, nose_tip_y), (right_eye_x, right_eye_y), (left_eye_x, left_eye_y))

        # Logic determines the direction of view
        if abs(left_eye_angle - right_eye_angle) < 0.25:

            cv2.putText(image, "Look straight ahead", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        elif left_eye_angle > right_eye_angle:
            cv2.putText(image, "Looking Left", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(image, "Looking Right", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)



    def process_frame(self, results, image):
        # try:
        landmarks = results.pose_landmarks.landmark
        # Get coordinates
        left_hip = [landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value].y]
        left_shoulder = [landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        left_elbow = [landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

        # Calculation angle
        angle = calculation_angle(left_hip, left_shoulder, left_elbow)

        # Visulize angle
        cv2.putText(image, str(round(angle, 2)), tuple(np.multiply(left_shoulder, (self.height, self.width)).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        return angle



    def Run_the_process(self):
        pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=1)
        while self.cap.isOpened():
            # while self.cap.isOpened():
            _, frame = self.cap.read()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                angle = self.process_frame(results, image)
                self.player_direction_view(results, image)
            except:
                continue

            # Curl counter logic
            if angle > 150:
                self.stage = "Down"
            if angle < 30 and self.stage == "Down":
                self.stage = "Up"
                self.counter += 1

            self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
            cv2.putText(image, str(self.counter), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2,
                        cv2.LINE_AA)
            cv2.imshow('FoxCode', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    test = ReceiveAction()
    test.Run_the_process()
