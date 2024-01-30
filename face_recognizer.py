import cv2
import requests
from datetime import datetime, timedelta
from typing import List, Tuple, Union
import numpy as np

frame_name: str = 'Attendance System'
api_url: str = 'http://127.0.0.1:5000/recognize_face'
face_id_list: List[Tuple[str, datetime]] = []
def recognize_faces(capture: Union[int, str] = 0) -> None:
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascade_path: str = "haarcascade_frontalface_default.xml"
    face_cascade: cv2.CascadeClassifier = cv2.CascadeClassifier(cascade_path)
    font: int = cv2.FONT_HERSHEY_SIMPLEX
    cam: cv2.VideoCapture
    if isinstance(capture, int):
        cam = cv2.VideoCapture(capture)
    else:
        cam = cv2.VideoCapture(capture)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
    cam.set(cv2.CAP_PROP_FPS, 25)

    min_w: float = 0.1 * cam.get(3)
    min_h: float = 0.1 * cam.get(4)
    while True:
        ret, img = cam.read()
        if not ret or img is None:
            print("Video ended or cannot be read. Exiting.")
            break
        gray: np.ndarray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces: np.ndarray = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(int(min_w), int(min_h)),)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            if confidence < 100:
                face_id: str = str(id)
                confidence = "  {0}%".format(round(100 - confidence))
                index: Union[None, int] = next((i for i, (fid, _) in enumerate(face_id_list) if fid == face_id), None)

                if index is not None:
                    _, last_time = face_id_list[index]
                    if (datetime.now() - last_time) > timedelta(minutes=30):
                        if send_attendance_request(face_id):
                            print(f"Face ID {face_id} recognized and marked attendance.")
                            face_id_list.pop(index)
                            face_id_list.append((face_id, datetime.now()))
                        else:
                            print(f"Failed to mark attendance for Face ID {face_id}.")
                else:
                    if send_attendance_request(face_id):
                        print(f"Face ID {face_id} recognized and marked attendance.")
                        face_id_list.append((face_id, datetime.now()))
                    else:
                        print(f"Failed to mark attendance for Face ID {face_id}.")
            else:
                face_id: str = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            cv2.putText(img, str(face_id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
        cv2.imshow(frame_name, img)
        k: int = cv2.waitKey(10) & 0xff
        if k == 27:
            break
    print("\n[INFO] Exiting Program ")
    cam.release()
    cv2.destroyAllWindows()
def send_attendance_request(face_id: str) -> bool:
    data: dict = {'face_id': face_id}
    try:
        response: requests.Response = requests.post(api_url, json=data)
        response.raise_for_status() 
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error while sending API request: {e}")
        return False
    
if __name__ == "__main__":
    recognize_faces(0)