import cv2
import numpy as np
import os

def train_model():
    trainer_dir = 'trainer'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    path = 'dataset'

    def get_images_and_labels(path):
        image_paths = [os.path.join(path, f) for f in os.listdir(path)]
        face_samples = []
        ids = []

        for image_path in image_paths:
            img_numpy = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            id = int(os.path.split(image_path)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                face_samples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)

        return face_samples, ids

    print("\n[INFO] Training faces. It will take a few seconds. Wait ...")
    faces, ids = get_images_and_labels(path)
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer/trainer.yml
    os.makedirs(trainer_dir, exist_ok=True)
    model_path = os.path.join(trainer_dir, 'trainer.yml')
    recognizer.write(model_path)

    # Print the number of faces trained and end the program
    print("\n[INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))

if __name__ == "__main__":
    train_model()
