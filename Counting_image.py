from ultralytics import YOLO
import cv2
import os


model = YOLO('yolov8n.pt')  

def detect_and_count_vehicles(image_path):
   
    results = model.predict(source=image_path, conf=0.5)  
    detections = results[0].boxes.data.tolist()
    vehicle_count = 0

    for detection in detections:
        class_id = int(detection[5])  
        if 2 <= class_id <= 7:  
            vehicle_count += 1 
            
    return vehicle_count


image_paths = ["C:/Users/samar/OneDrive/Desktop/CODING/Python/Mynewproj/Smart-Traffic-Management/Cars Images/cars1.jpg", "C:/Users/samar/OneDrive/Desktop/CODING/Python/Mynewproj/Smart-Traffic-Management/Cars Images/cars2.jpg", "C:/Users/samar/OneDrive/Desktop/CODING/Python/Mynewproj/Smart-Traffic-Management/Cars Images/cars3.jpg","C:/Users/samar/OneDrive/Desktop/CODING/Python/Mynewproj/Smart-Traffic-Management/Cars Images/cars4.jpg","C:/Users/samar/OneDrive/Desktop/CODING/Python/Mynewproj/Smart-Traffic-Management/Cars Images/cars5.jpg"] 
vehicle_counts = []  
count=1
for image_path in image_paths:
    if os.path.exists(image_path):
        vehicle_count = detect_and_count_vehicles(image_path)
        vehicle_counts.append(vehicle_count)  
        print(f"Vehicles detected in road number {count}: {vehicle_count}")
        count=count+1
    else:
        print(f"Image not found: {image_path}")
count=0

print("Vehicle counts for each road:", vehicle_counts)