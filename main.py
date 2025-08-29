import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

def main():
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 40)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 50)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('frame', frame)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()