from fastapi import APIRouter, HTTPException
from models import Student, StudentUpdate
from datetime import datetime
from storage import read_data, write_data, generate_id, STUDENTS_FILE

router= APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.get("/")
def get_students():
    return read_data(STUDENTS_FILE)

@router.get("/{student_id}")
def get_student(student_id: int):
    students= read_data(STUDENTS_FILE)
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail=f"Student with id {student_id} not found")

@router.post("/")
def create_student(student : Student):
    students=read_data(STUDENTS_FILE)
    new_student = {
        "id":generate_id(students),
        "name": student.name,
        "age": student.age,
        "grade": student.grade,
        "created_at":datetime.now().isoformat(),
        "updated_at":datetime.now().isoformat()
    }
    student.append(new_student)
    write_data(STUDENTS_FILE,students)
    return new_student

@router.put("/{student_id}")
def update_student (student_id: int , updated: StudentUpdate):
    students = read_data(STUDENTS_FILE)
    for student in students:
        if student["id"]==student_id:
            if updated.name is not None:
                student["name"]= updated.name
            if updated.age is not None:
                student["age"]=updated.age
            if updated.grade is not None:
                student["grade"]=updated.grade
            student["updated_at"]=datetime.now().isoformat()
            write_data(STUDENTS_FILE, students)
            return student
    raise HTTPException(status_code=404 , detail= f"Student with id {student_id} not found")

@router.delete("/{student_id}"):
def delete_student(student_id:int):
    students=read_data(STUDENTS_FILE)
    for student in students:
        if student["id"]== student_id:
            students.remove(student)
            write_data(STUDENTS_FILE,students)
            return {"message":"Student '{student['name']}' deleted successfully!"}
    raise HTTPException(status_code=404 , detail=f"Student with id {student_id} not found")