from ultralytics import YOLO

model = YOLO('yolov8n.pt')

model.train(data=r'/home/szewczyk/Desktop/dataset.yaml', epochs=2, imgsz=320)