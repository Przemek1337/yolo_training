from ultralytics import YOLO

# Wczytanie modelu YOLOv8
model = YOLO('yolov8n.pt')  # Wybierz model YOLOv8 (nano, small, medium, etc.)

# Trenowanie modelu
model.train(data=r'C:\Users\przem\PycharmProjects\yolo_training\dataset.yaml', epochs=10, imgsz=320)