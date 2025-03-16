import sqlite3
import os

DB_NAME = "artrelic.db"

def get_connection():
    """Connects to SQLite3 database, creates one if it doesn't exist."""
    connection = None
    try:
        db_exists = os.path.exists(DB_NAME)
        connection = sqlite3.connect(DB_NAME)

        if not db_exists:
            print(f"Database '{DB_NAME}' created successfully.")
        else:
            print(f"Connected to existing database '{DB_NAME}'.")

        return connection  # Connection will be managed by caller function

    except sqlite3.Error as e:
        print(f"Error while connecting to database: {e}")
        return None
    