from flask import Flask, render_template, request, flash, jsonify  # Updated import
from mongo_operation import insert_users,insert_location

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/submit_user_info', methods=['POST'])
def submit_user_info():
    data = request.form
    name = data.get('name')
    age = data.get('age')
    print(f"Received name: {name}, age: {age}")
    insert_users({'name': name, 'age': age})
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