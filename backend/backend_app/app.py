from flask import Flask, render_template, request, flash, jsonify  # Updated import
from mongo_operation import insert_users,insert_location
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/submit_user_info', methods=['POST'])
def submit_user_info():
    data = request.form
    created_at = datetime.datetime.now()
    user_name = data.get('user_name')
    date_of_birth = data.get('date_of_birth')
    email = data.get('email')
    phone = data.get('phone')
    region = data.get('region')
    field_of_interst = data.get('field_of_interst')
    field_of_research = data.get('field_of_research')
    curently_working = data.get('curently_working')
    graduaction_type = data.get('graduaction_type')
    graduaction_year = data.get('graduaction_year')
    graduaction_course = data.get('graduaction_course')
    # print(f"Received name: {name}, age: {age}")
    # insert_users({'name': name, 'age': age})
    return {"message":"User information submitted successfully!"}  # Use flash for alerts  # Render the template to display the alert

@app.route('/submit_device_info', methods=['POST'])
def submit_device_info():
    data = request.json
    device = data.get('device')
    location = data.get('location')
    insert_location({'device': device, 'location': location})
    print(f"Received device: {device}, location: {location}")
    return jsonify({"message": "Device and location information received successfully!"})

if __name__ == '__main__':
    app.run(debug=True)