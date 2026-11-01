
from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

def connect_db():
    for i in range(10):
        try:
            return mysql.connector.connect(
                host="db",
                user="appuser",
                password="apppass",
                database="studentdb"
            )
        except mysql.connector.Error:
            print("Waiting for database...")
            time.sleep(3)

    raise Exception("Database connection failed")


@app.route("/")
def home():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    result = "<h1>Student Management System</h1>"
    result += "<h2>Student Details</h2>"
    result += "<table border='1' cellpadding='10'>"
    result += "<tr><th>ID</th><th>Name</th><th>Department</th></tr>"

    for student in students:
        result += f"<tr><td>{student[0]}</td>"
        result += f"<td>{student[1]}</td>"
        result += f"<td>{student[2]}</td></tr>"

    result += "</table>"

    cursor.close()
    db.close()
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
