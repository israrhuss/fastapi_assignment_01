from fastapi import FastAP
from pydantic import BaseModel

app = FastAPI()


students = []

class Student(BaseModel):
    id: int
    name: str
    age: int
    marks: int

@app.get("/students/")
def all_students():
    return students

@app.post("/addStudents/")
def create_student(student: Student):
    students.append(student)
    return students

@app.delete("/deleteStudent/{student_id}")
def delete_student(student_id: int):
    global students
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "Student deleted successfully"}
    

@app.get("/getStudent/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return students
    

@app.put("/updateStudent/{student_id}")
def update_student(student_id: int, updated_student: Student):
    global students
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students[index] = updated_student
            return {"message": "Student is successfully updated"}