# RUN THE PROJECT : 1. ctrl + ~ (open terminal)   2.python -u "c:\Users\Niharika\OneDrive\Desktop\gauntlet-control-system\src\main.py"

import cv2
from hand_detector import HandDetector
from gesture_logic import fingers_up
import pygame

pygame.mixer.init()

FPS = 30

GESTURE_DURATION = {
    "half_population_disappears": 3,
    "full_population": 5,

    "space": 3,
    "mind": 3,
    "reality": 3,
    "power": 3,
    "time": 3,
    "soul": 3,

    "gauntlet_with_all_the_stones": 3
}

GESTURE_IMAGES = {
    "half_population_disappears": "assets/pics/half_population_disappears.jpg",
    "full_population": "assets/pics/full_population.jpg",

    "space": "assets/pics/space.jpg",
    "mind": "assets/pics/mind.jpg",
    "reality": "assets/pics/reality.jpg",
    "power": "assets/pics/power.jpg",
    "time": "assets/pics/time.jpg",
    "soul": "assets/pics/soul.jpg",

    "gauntlet_with_all_the_stones": "assets/pics/gauntlet_with_all_the_stones.jpg",
}

SOUNDS = {
    "half_population_disappears": pygame.mixer.Sound("assets/sounds/destroy.wav"),
    "full_population": pygame.mixer.Sound("assets/sounds/earth.wav"),

    "space": pygame.mixer.Sound("assets/sounds/stones.wav"),
    "mind": pygame.mixer.Sound("assets/sounds/stones.wav"),
    "reality": pygame.mixer.Sound("assets/sounds/stones.wav"),
    "power": pygame.mixer.Sound("assets/sounds/stones.wav"),
    "time": pygame.mixer.Sound("assets/sounds/stones.wav"),
    "soul": pygame.mixer.Sound("assets/sounds/stones.wav"),

    "gauntlet_with_all_the_stones": pygame.mixer.Sound("assets/sounds/gauntlet.wav"),
}

images = {}
for key, path in GESTURE_IMAGES.items():
    img = cv2.imread(path)
    if img is not None:
        images[key] = cv2.resize(img, (640, 480))

cap = cv2.VideoCapture(0)
detector = HandDetector()

cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)
cv2.namedWindow("Infinity Result", cv2.WINDOW_NORMAL)

locked_gesture = None
last_gesture = None
lock_frames = 0

def draw_hud(frame, hands, fingers, gesture, lock_frames):
    y = 30
    dy = 30

    cv2.putText(frame, f"Hands: {hands}", (20, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    y += dy

    cv2.putText(frame, f"Fingers: {fingers}", (20, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    y += dy

    if gesture:
        cv2.putText(frame, f"Gesture: {gesture.upper()}", (20, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
        y += dy

    if lock_frames > 0:
        cv2.putText(frame, f"LOCKED: {lock_frames//FPS}s", (20, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

while True:
    success, frame = cap.read()
    if not success:
        break

    result = detector.detect(frame)

    total_fingers = 0
    fist_count = 0
    palm_count = 0

    if result.hand_landmarks:
        for i, hand in enumerate(result.hand_landmarks):
            label = result.handedness[i][0].category_name
            fingers = fingers_up(hand, label)
            count = sum(fingers)

            total_fingers += count
            if count == 0:
                fist_count += 1
            if count == 5:
                palm_count += 1

    gesture = None

    if fist_count == 2:
        gesture = "full_population"
    elif fist_count == 1 and total_fingers == 0:
        gesture = "half_population_disappears"
    elif palm_count == 2:
        gesture = "gauntlet_with_all_the_stones"
    elif total_fingers == 1:
        gesture = "space"
    elif total_fingers == 2:
        gesture = "mind"
    elif total_fingers == 3:
        gesture = "reality"
    elif total_fingers == 4:
        gesture = "power"
    elif total_fingers == 5:
        gesture = "time"
    elif total_fingers == 6:
        gesture = "soul"

    if gesture and gesture != last_gesture:
        locked_gesture = gesture
        last_gesture = gesture

        lock_frames = GESTURE_DURATION.get(gesture, 3) * FPS

        pygame.mixer.stop()
        if gesture in SOUNDS:
            SOUNDS[gesture].play()

    draw_hud(
        frame,
        hands=len(result.hand_landmarks) if result.hand_landmarks else 0,
        fingers=total_fingers,
        gesture=locked_gesture,
        lock_frames=lock_frames
    )

    cv2.imshow("Camera Feed", frame)

    if lock_frames > 0 and locked_gesture in images:
        cv2.imshow("Infinity Result", images[locked_gesture])
        lock_frames -= 1
    else:
        blank = frame.copy()
        blank[:] = 0
        cv2.imshow("Infinity Result", blank)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()


