from flask import Flask,render_template,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///face_recognition_db.sqlite'
db = SQLAlchemy(app)

class FaceRecognition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    face_id = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

def save_to_database(face_id):
    last_entry = FaceRecognition.query.filter_by(face_id=face_id).order_by(FaceRecognition.timestamp.desc()).first()
    if last_entry and (datetime.now() - last_entry.timestamp) < timedelta(hours=120):
        print(f"Skipping entry for FaceID {face_id} as less than 12 hours have passed.")
        return
    new_entry = FaceRecognition(face_id=face_id, timestamp=datetime.now())
    db.session.add(new_entry)
    db.session.commit()

@app.route('/recognize_face', methods=['POST'])
def recognize_face():
    data = request.json
    face_id = data.get('face_id')

    if face_id:
        save_to_database(face_id)
        return jsonify({"message": "Face recognized and saved successfully."}), 200
    else:
        return jsonify({"error": "Face ID not provided."}), 400

@app.route('/')
def index():
    twelve_hours_ago = datetime.now() - timedelta(hours=12)
    entries = FaceRecognition.query.filter(FaceRecognition.timestamp >= twelve_hours_ago).order_by(FaceRecognition.timestamp.desc()).all()

    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()
    app.run(debug=True)