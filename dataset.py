import cv2
import os

# def create_dataset(video_path):
#     cam = cv2.VideoCapture(video_path)
#     face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#     frame_count = 0
#     processing_interval = 4 
#     while True:
#         try:
#             face_id = int(input('\nEnter user ID (press -1 to stop and train): '))
#             if face_id == -1:
#                 break
#         except ValueError:
#             print("Invalid input. Please enter a numeric ID.")
#             continue
        
#         print(f"\n[INFO] Initializing face capture for User {face_id}. Look at the video and wait...")
#         count = 0
#         dataset_dir = 'dataset/'
#         os.makedirs(dataset_dir, exist_ok=True)

#         while True:
#             ret, img = cam.read()
#             if not ret:
#                 print("Video ended or cannot be read. Exiting.")
#                 break

#             frame_count += 1
#             if frame_count % processing_interval != 0:
#                 continue

#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

#             for (x, y, w, h) in faces:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#                 count += 1
#                 cv2.imwrite(f"{dataset_dir}User.{face_id}.{count}.jpg", gray[y:y + h, x:x + w])
            
#             # Resize the frame to 400x400
#             resized_frame = cv2.resize(img, (400, 400))

#             cv2.imshow('image', resized_frame)

#             k = cv2.waitKey(1) & 0xff 
#             if k == 27 or count >= 30:
#                 break

#         print(f"\n[INFO] Data collection for User {face_id} completed.")

#     print("\n[INFO] Exiting Program and cleanup stuff")
#     cam.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     video_path = 'self.mp4' 
#     create_dataset(video_path)

index = 0
arr = []
while True:
    print(arr)
    cap = cv2.VideoCapture(index)
    if not cap.read()[0]:
        break
    else:
        arr.append(index)
    cap.release()
    index += 1
    
    