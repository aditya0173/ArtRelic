# Import Libraries
from flask import Flask, render_template, request, jsonify
from mongo_operation import insert_users, insert_location
import datetime
import random
import string
import pymongo

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB setup for unique user_id check
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["relic"]
users_collection = db["users"]

# Generate Unique UserId function
def generate_unique_user_id():
    while True:
        user_id = 'USR_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        if not users_collection.find_one({'user_id': user_id}):
            return user_id

# Routes for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Routes for submit_user_info
@app.route('/submit_user_info', methods=['POST'])
def submit_user_info():
    data = request.form
    created_at = datetime.datetime.now()
    user_id = generate_unique_user_id()

    user_data = {
        'user_id': user_id,
        'user_name': data.get('user_name'),
        'date_of_birth': data.get('date_of_birth'),
        'email': data.get('email'),
        'phone': data.get('phone'),
        'region': data.get('region'),
        'field_of_interest': data.get('field_of_interst'),  # Keep spelling if frontend has same
        'field_of_research': data.get('field_of_research'),
        'currently_working': data.get('curently_working'),
        'graduation_type': data.get('graduaction_type'),
        'graduation_year': data.get('graduaction_year'),
        'graduation_course': data.get('graduaction_course'),
        'created_at': created_at
    }

    # print(f"Received name: {name}, age: {age}")
    # insert_users({'name': name, 'age': age})
    insert_users(user_data)
    return jsonify({"message": "User information submitted successfully!", "user_id": user_id})

# Routes for submit_device_info
@app.route('/submit_device_info', methods=['POST'])
def submit_device_info():
    data = request.json
    device = data.get('device')
    location = data.get('location')
    insert_location({'device': device, 'location': location})
    print(f"Received device: {device}, location: {location}")
    return jsonify({"message": "Device and location information received successfully!"})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
