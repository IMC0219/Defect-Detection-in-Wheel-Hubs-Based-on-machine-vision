import time

from ultralytics import YOLO
model = YOLO("./yolov8n.pt")
results = model.train(data='datasets/data.yaml',epochs=3,imgsz=640,device=[0,],workers=0,batch=4,cache=True)
time.sleep(10)