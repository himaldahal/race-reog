# 👨‍💼 Facial Attendance System

This project is a facial attendance system that utilizes Flask for the backend, Bootstrap 5 for the frontend, and OpenCV for face detection and recognition.

## Project Structure

<pre>📦 facial-attendance-system
├─ backend
│  ├─ app.py
│  ├─ instance
│  │  └─ face_recognition_db.sqlite
│  └─ templates
│     └─ index.html
├─ dataset.py
├─ face_recognizer.py
├─ haarcascade_frontalface_default.xml
├─ trainer.py
├─ trainer
│  └─ trainer.yml
└─ webcam_dataset.py
</pre>

## Features

*   🔧 Backend developed with Flask
*   🎨 Webpage styled using Bootstrap 5
*   👤 Facial detection and recognition using OpenCV
*   📸 Dataset gathering through webcam or images
*   📊 Model training for accurate recognition
*   📝 Attendance marking based on recognized faces

## Usage

1.  📸 Run `dataset.py` or `webcam_dataset.py` to gather photos for the dataset.
2.  🚀 Run `trainer.py` to train the model using the gathered dataset.
3.  ⚙️ Ensure that the Flask server is running by executing `python3 app.py`.
4.  👀 Run `face_recognizer.py` to recognize faces and mark attendance.

To run the Flask server:

    python3 app.py

Access the web interface at [http://localhost:5000](/).

## Installation

You can install the required packages using pip3\. Run the following command:

    pip3 install Flask opencv-python opencv-contrib-python requests

## Contributing

🤝 Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
