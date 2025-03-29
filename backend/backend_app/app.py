from flask import Flask, render_template, request, flash, jsonify  # Updated import
from mongo_operation import insert_users

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
    return flash("User information submitted successfully!")  # Use flash for alerts  # Render the template to display the alert

if __name__ == '__main__':
    app.run(debug=True)
