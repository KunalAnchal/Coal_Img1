from ultralytics import YOLO
import cv2

model = YOLO("coal_29ju.pt")
model.predict(source="img.jpg", show=True)
cv2.waitKey(0)