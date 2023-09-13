from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Establish a MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Replace with your MySQL password
    database="student"
)

# Create a cursor object
cursor = mydb.cursor()

# Define a Pydantic model for StudentData
class StudentData(BaseModel):
    id: int
    name: str
    email: str

# Endpoint to fetch student data
@app.get("/students/", response_model=List[StudentData])
def get_students():
    # Execute SQL query to fetch students
    cursor.execute("SELECT * FROM students")
    
    # Fetch the result
    students = cursor.fetchall()
    
    # Convert the result to a list of dictionaries
    student_data = [{"id": id, "name": name, "email": email} for id, name, email in students]
    
    return student_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
