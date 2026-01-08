import os
import cv2
from ultralytics import YOLO

# Absolute path to project root (shortss/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Absolute path to model file
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pt")

print("Loading YOLO model from:", MODEL_PATH)

model = YOLO(MODEL_PATH)
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        results = model(frame, conf=0.5, device="cpu")
        annotated = results[0].plot()

        _, buffer = cv2.imencode(".jpg", annotated)
        frame = buffer.tobytes()

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
