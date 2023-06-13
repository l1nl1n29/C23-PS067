from flask import Flask, request, jsonify, session, 
from flask_restful import Resource, Api
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import random
import os
import tensorflow as tf
import json
import numpy as np
import base64
import matplotlib.pyplot as plt
import pymysql
import jwt

pymysql.install_as_MySQLdb()

app = Flask(__name__)
api = Api(app)
CORS(app)
app.secret_key = "Seasee-GLOBALE"
model = tf.keras.models.load_model('./model/mymodel.h5')

# Specify the upload directory
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set SQLAlchemy database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@34.128.78.143/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the authentication model schema (login, register)
class AuthModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.column(db.String(100))

# Function to check allowed file extensions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Register user endpoint
class RegisterUser(Resource):
    def post(self):
        data = request.form
        dataUsername = data.get('username')
        dataPassword = data.get('password')
        dataEmail = data.get('email')

        # Check if username and password exist
        if dataUsername and dataPassword:
            # Save authentication data to the database
            authData = AuthModel(username=dataUsername, password=dataPassword, email=dataEmail)
            db.session.add(authData)
            db.session.commit()
            return {"error": False, "message": "User Created"}, 200
        return {"message": "Username/password cannot be empty"}, 400

# Login user endpoint
# Login user endpoint
class LoginUser(Resource):
    def post(self):
        data = request.form
        dataUsername = data.get('username')
        dataPassword = data.get('password')

        # Check if username and password match
        user = AuthModel.query.filter_by(username=dataUsername, password=dataPassword).first()
        if user:
            # Generate JWT token
            token = jwt.encode({'userId': user.id, 'name': user.username}, app.secret_key, algorithm='HS256')
            return {
                "error": False,
                "message": "success",
                "loginResult": {
                    "userId": user.id,
                    "name": user.username,
                    "token": token
                }
            }, 200
        return {"message": "Login failed. Please try again"}, 401

# Logout user endpoint
class LogoutUser(Resource):
    def get(self):
        session.pop('token', None)
        return {"message": "Logout successful"}, 200

# Upload image endpoint
class UploadImage(Resource):
    def post(self):
        # Check if token is present
        if 'Authorization' not in request.headers:
            return {"message": "Authorization token is missing"}, 401

        # Extract the token from the Authorization header
        token = request.headers['Authorization'].split()[1]

        try:
            # Verify the token
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            current_identity = decoded_token['username']
        except jwt.InvalidTokenError:
            return {"message": "Invalid token"}, 401

        # file = '../Model/images/laptop.jpg'
        image = generate_image_from_base64(
            request.form["title"], request.form["body"])
        img = tf.keras.preprocessing.image.load_img(image, target_size=(150, 150))
        x = tf.keras.preprocessing.image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        history = model.predict(images)
        print(history)
        os.remove(get_filename(request.form["title"]))
        predict = ""
        if history[0]>0.5:
            predict = "is a Trash" 
        else:
            predict = "is a Coral"

        return {
            "title": request.form["title"],
            "body": predict
        }
    
def generate_image_from_base64(filename, string):
    file = open('./{filename}.jpg'.format(filename=filename), 'wb')
    file.write(base64.b64decode((string)))
    file.close()
    return './{filename}.jpg'.format(filename=filename)

def get_filename(filename):
    return './{filename}.jpg'.format(filename=filename)


# Capture image endpoint
class CaptureImage(Resource):
    def post(self):
        # Perform image capture using camera 
        captured_image_path = "/path/to/captured/image.jpg"  # Path to the captured image file

        # Perform classification on the captured image
        classification_result = classify_image(captured_image_path)

        return jsonify({"message": "Image captured successfully", "classification": classification_result}), 200

# Function to classify the image
def classify_image(image_path):

    # Randomly assign "Trash" or "Coral" classification
    classifications = ["Trash", "Coral"]
    classification_result = random.choice(classifications)

    return classification_result

# Initialize the database and create tables
def initialize_database():
    with app.app_context():
        db.create_all()

# API routes
api.add_resource(RegisterUser, "/api/register", methods=["POST"])
api.add_resource(LoginUser, "/api/login", methods=["POST"])
api.add_resource(LogoutUser, "/api/logout", methods=["GET"])
api.add_resource(UploadImage, "/api/upload", methods=["POST"])
api.add_resource(CaptureImage, "/api/capture", methods=["POST"])

# Run the application
if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
