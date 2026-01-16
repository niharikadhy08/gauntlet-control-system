# 🧤 Gauntlet Control System

A **computer vision–based hand gesture control system** inspired by the **Infinity Gauntlet** from Marvel’s *Avengers*.

This project uses **MediaPipe**, **OpenCV**, and **Pygame** to detect hand gestures in real time using a webcam and map them to **Infinity Stones, Gauntlet states, images, and sound effects** — creating an interactive, demo-ready experience.

---

## Concept & Inspiration

In the Marvel universe, the Infinity Gauntlet derives its power from six Infinity Stones.
Similarly, in this project:

* **Finger-count gestures (1–6 fingers)** represent the six Infinity Stones
* **Gauntlet states** are triggered using specific multi-hand gestures
* A **single fist** represents the infamous snap (half the universe disappears)
* **Two fists** represent a stable universe
* **Two open palms** represent the Gauntlet with all stones collected

---

## Gesture Mapping Logic

| Gesture                | Action                                      |
| ---------------------- | ------------------------------------------- |
| 1 fist (0 fingers)     | 💥 Half the universe disappears             |
| 2 fists                | 🌍 Full population (stable universe)        |
| 1 finger               | 🟦 Space Stone                              |
| 2 fingers              | 🟨 Mind Stone                               |
| 3 fingers              | 🔴 Reality Stone                            |
| 4 fingers              | 🟪 Power Stone                              |
| 5 fingers              | 🟩 Time Stone                               |
| 6 fingers (both hands) | 🟠 Soul Stone                               |
| 2 open palms           | 🧤 Infinity Gauntlet (all stones collected) |

Each gesture:

* Displays a **themed image**
* Plays a **corresponding sound effect**
* Is **locked for a few seconds** to prevent flickering or false triggers

---

## Features

* 🖐️ Real-time hand and finger detection
* 🎯 Accurate gesture classification using landmark-based logic
* 🧠 On-screen HUD showing hands detected, finger count, and active gesture
* 🖼️ Separate result window for visual feedback
* 🔊 Sound effects synced with gestures
* ⏱️ Gesture locking for stable interaction
* 🧱 Clean, modular architecture (`hand_detector`, `gesture_logic`, `main`)

---

## Tech Stack

* **Python 3.10+**
* **OpenCV** – video capture and rendering
* **MediaPipe Tasks** – hand landmark detection
* **Pygame** – audio playback
* **Webcam**

---

## Project Structure

```
gauntlet-control-system/
│
├── src/
│   ├── main.py              # Application entry point
│   ├── hand_detector.py     # MediaPipe hand detection wrapper
│   └── gesture_logic.py     # Finger state & gesture logic
│
├── assets/
│   ├── pics/                # Gesture images
│   └── sounds/              # Gesture sound effects
│
├── models/
│   └── hand_landmarker.task
│
├── venv/
└── README.md
```

---

## How to Run

### 1️⃣ Activate virtual environment

```
venv\Scripts\activate
```

### 2️⃣ Install dependencies

```
python -m pip install opencv-python mediapipe pygame
```

### 3️⃣ Run the project

```
python src/main.py
```

Press **ESC** to exit the application.

---

## Demo Usage Tips

* For **accurate finger detection**, keep the **back side of your palm facing the camera** (palm facing away)
* Hold gestures steady for **1–2 seconds**
* Ensure **good lighting** for best landmark detection accuracy
