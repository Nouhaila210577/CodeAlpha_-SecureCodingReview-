# This is a vulnerable script for security testing 
import sqlite3

def register():
    username = input("Choose a username: ")  # Any input accepted as username (length, characters, format)
    password = input("Choose a password: ")  # No hashing, password exposed

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SQL Injection risk (string concatenation)
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    conn.commit()

    print("User registered!")  # No check if user already exists
    conn.close()


def show_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # No access control: anyone can view all users (Sensitive data exposed)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)  # Passwords exposed in clear text

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
