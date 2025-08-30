import cv2
import numpy as np
from matplotlib import pyplot as plt
from ultralytics import YOLO

cap = cv2.VideoCapture(0)

def main():
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 40)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 50)

    model = YOLO("yolov8n.pt")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]

        annotated_frame = results.plot()

        cv2.imshow("YOLOv8 Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()