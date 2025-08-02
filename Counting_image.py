from ultralytics import YOLO
import os

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Path to the folder containing vehicle images
image_folder = "C:/Users/samar/OneDrive/Desktop/CODING/Python/Mynewproj/Smart-Traffic-Management/Cars Images"

# List of image filenames
image_files = ["cars1.jpg", "cars2.jpg", "cars3.jpg", "cars4.jpg", "cars5.jpg"]

# Function to detect and count vehicles in an image
def detect_and_count_vehicles(image_path):
    results = model.predict(source=image_path, conf=0.5)
    detections = results[0].boxes.data.tolist()
    vehicle_count = 0
    for detection in detections:
        class_id = int(detection[5])
        if 2 <= class_id <= 7:  # Classes 2 to 7 are vehicle classes in COCO
            vehicle_count += 1
    return vehicle_count

# Process all images
vehicle_counts = []
for i, file in enumerate(image_files):
    full_path = os.path.join(image_folder, file)
    if os.path.exists(full_path):
        count = detect_and_count_vehicles(full_path)
        vehicle_counts.append(count)
        print(f"Vehicles detected in road number {i+1}: {count}")
    else:
        print(f"Image not found: {full_path}")

print("Vehicle counts for each road:", vehicle_counts)
