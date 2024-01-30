import os
import cv2

def create_dataset(camera_index=0):
    cam = cv2.VideoCapture(camera_index)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while True:
        try:
            face_id = int(input('\nEnter user ID (press -1 to stop and train): '))
            if face_id == -1:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")
            continue

        print(f"\n[INFO] Initializing face capture for User {face_id}. Look at the camera and wait...")

        # Initialize individual sampling face count
        count = 0

        # Create the dataset directory if it doesn't exist
        dataset_dir = 'dataset/'
        os.makedirs(dataset_dir, exist_ok=True)

        while True:
            ret, img = cam.read()
            if not ret:
                print("Error reading from the camera. Exiting.")
                break

            img = cv2.flip(img, -1)  # flip video image vertically
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                count += 1

                # Save the captured image into the datasets folder
                cv2.imwrite(f"{dataset_dir}User.{face_id}.{count}.jpg", gray[y:y + h, x:x + w])

                # Display the image (optional, comment out if not needed)
                cv2.imshow('image', img)

            k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
            if k == 27 or count >= 30:  # Take 30 face samples or press 'ESC' to stop
                break

        print(f"\n[INFO] Data collection for User {face_id} completed.")

    print("\n[INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_dataset()
