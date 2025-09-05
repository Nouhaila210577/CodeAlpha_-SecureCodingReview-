# Secure version of the vulnerable script 
import sqlite3
import hashlib
import re

DB_NAME = "users.db"

#  Hash password using SHA-256 
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Choose a username: ")
    # Validate username (3-20 characters, only letters/numbers/underscore)
    if not re.fullmatch(r'\w{3,20}', username):
        print("Invalid username. (Use 3-20 letters, numbers, or underscore).\n")
        return

    password = input("Choose a password: ")

    # Hash password before storing
    hashed_password = hash_password(password)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    try:
        # Secure query execution with parameters to prevent SQL injection
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print("User registered!\n")
    except sqlite3.IntegrityError:     # Check if username already exists
        print("Username already exists.\n")
    finally:
        conn.close()

def show_users():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Only show usernames, no passwords exposed
    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()
    for user in users:
        print(f"Username: {user[0]}")

    conn.close()

while True:
    print("\n1. Register")
    print("2. Show users")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        show_users()
    elif choice == "3":
        break
    else:
        print("Invalid choice")