import sqlite3
from get_connection import get_connection

def create_users_table():
    connection = get_connection()  # Get database connection
    if not connection:
        print({"status": "error", "message": "Database connection failed."})
        return
    
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
    """
    
    try:
        cursor.execute(create_table_query)  # Execute before closing connection
        connection.commit()
        
        response = {
            "status": "success",
            "message": "Users table created successfully (if not existed)."
        }

    except sqlite3.Error as e:
        response = {
            "status": "error",
            "message": f"Error while creating Users table: {e}"
        }

    finally:
        if connection:
            connection.close()  # Close connection here
    
    print(response)
    return response

if __name__ == "__main__":
    create_users_table()
