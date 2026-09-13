import cv2
import os
import shutil

video_path = r"c:\Users\LENOVO\Desktop\Wimprove\Laptop_morphing_into_robot_and_20260911101613.mp4"
frames_dir = r"c:\Users\LENOVO\Desktop\Wimprove\frames"

if os.path.exists(frames_dir):
    shutil.rmtree(frames_dir)
os.makedirs(frames_dir)

print(f"Extracting frames from {video_path}...")

cap = cv2.VideoCapture(video_path)
count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Save as webp
    frame_path = os.path.join(frames_dir, f"frame_{count:04d}.webp")
    cv2.imwrite(frame_path, frame, [cv2.IMWRITE_WEBP_QUALITY, 80])
    count += 1

cap.release()
print(f"Extracted {count} frames successfully.")
