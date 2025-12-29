from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="secret_password",
        database="user_db"
    )

@app.route('/add/<name>')
def add_user(name):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(255))")
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    return f"User {name} added!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)