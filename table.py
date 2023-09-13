from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel
from typing import List

app = FastAPI()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="student"
)

#
cursor = mydb.cursor()

class StudentData(BaseModel):
    id: int
    name: str
    email: str


@app.get("/students/", response_model=List[StudentData])
def get_students():
  
    cursor.execute("SELECT * FROM students")
    
    
    students = cursor.fetchall()
    
    
    student_data = [{"id": id, "name": name, "email": email} for id, name, email in students]
    
    return student_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
