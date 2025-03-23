# 🚀 User Guide: Setting Up Flask Backend & Database

## 📌 Introduction to Flask
Flask is a lightweight and flexible Python web framework that makes it easy to build web applications. It provides essential tools and features while keeping the core simple and extensible. Perfect for small and medium-sized projects! 💡

---

## 🛠️ Setting Up the Flask Backend

### 1⃣ Create a Virtual Environment
Before setting up Flask, it's a good practice to create a virtual environment:
```bash
python -m venv artrelicvenv
```
Activate the virtual environment:
- **Windows:**
  ```bash
  artrelicvenv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source artrelicvenv/bin/activate
  ```

### 2⃣ Install Dependencies
Inside the virtual environment, install Flask and SQLite dependencies:
```bash
pip install flask flask_sqlalchemy
```

---

## 🛄 Database Setup (SQLite)
### 3⃣ Creating the Database
Inside `backend_app/database/`, create a file `create_tables.py` and add the following code:
```python
import sqlite3

def create_users_table():
    connection = sqlite3.connect("artrelic.db")
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        user_id varchar(255),
        created_at timestamp,
        user_name varchar(255),
        eamil varchar(255),
        phone varchar(255),
        region varchar(255),
        field_of_intrest text,
        field_of_resarch text,
        currently_working text,
        graduaction_type varchar(255),
        graduaction_year year,
        graduaction_cource text,
        projects varchar(255),
        project_description text
        );
    """
    
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()
    print("✅ Users table created successfully!")

if __name__ == "__main__":
    create_users_table()
```
Run the script:
```bash
python backend_app/database/create_tables.py
```
This will create `artrelic.db` and the necessary `Users` table.

---

## 🚀 Running the Flask App
### 4⃣ Create `app.py`
Inside the main directory, create `app.py` and add:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to ArtRelic Backend! 🚀"

if __name__ == "__main__":
    app.run(debug=True)
```

### 5⃣ Run the Flask App
```bash
python app.py
```
Your Flask app will start running at:
```
http://127.0.0.1:5000/
```
Open this URL in your browser to see the welcome message! 🎉

---

## 🎯 Conclusion
Now you have a fully functional Flask backend with an SQLite database. You can expand it further by adding APIs, authentication, and more features!

🔥 **Happy Coding!** 🚀

---

## ⚠️ Notice
This project is currently in the **development stage** and has not yet been deployed for production use. If you plan to use it in production, make sure to modify `app.py` accordingly, including security enhancements and proper configurations. ⚠️

---

## 👨‍💻 Developers & Contribution

**👤 Developer: Adarsh Kumar**  
- 🔗 Connect on LinkedIn: [Adarsh Kumar](https://www.linkedin.com/in/adarsh-kumar-510a622b8/)  
- 🌎 Explore other projects: [GitHub - Adarsh21-dev](https://github.com/Adarsh21-dev)

**👤 Project In-Charge: Aditya Singh**  
- 🔗 Connect & Contribute: [GitHub - Aditya Singh](https://github.com/aditya0173/ArtRelic/tree/aditya_frontend_database)
