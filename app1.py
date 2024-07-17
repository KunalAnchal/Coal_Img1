from ultralytics import YOLO
import cv2

model = YOLO("coal_29ju.pt")
model.predict(source="coal-J29.mp4", show=True)
cv2.waitKey(0)
