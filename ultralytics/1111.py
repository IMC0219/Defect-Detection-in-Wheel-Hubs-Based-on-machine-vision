from ultralytics import YOLO
yolo = YOLO("./yolov8n.pt", task="detect")
result = yolo(source="E:\yolov8-main/ultralytics/assets/zidane.jpg", save=True)