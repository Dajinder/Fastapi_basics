from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


# students dictionary with different student details
students = {
    1: {"name":"Dajinder", "age":27, "intake":"Jan 2025"},
    2: {"name":"John", "age":22, "intake":"may 2025"},
    3: {"name":"Sam", "age":25, "intake":"Jan 2025"},
    4: {"name":"Michal", "age":20, "intake":"Sep 2024"}
}


class stdent(BaseModel):
    name:str
    age:int
    intake:str



class update_student(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    intake: Optional[str] = None


# root or home location
@app.get("/")
def index():
    return {"Hello":"World"}


#path parameter
@app.get("/student/{student_id}")
def get_student(student_id: int=Path(description="provide student ID", gt=0, lt=10)):
    return students[student_id]


# other parameters of path
# gt = greater than
# lt = less than
# ge = greater than or equal to
# le = less than or equal to


# query parameter
@app.get("/student_by_name")
def get_by_name(*, name: Optional[str] = None, test: Optional[int]=None): # None in parameter makes the field not required, use Optional as best practice as per fastapi
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data":"Not found"}

# in case of multiple parameters, optional parameter cannot be before required parameter
# def get_by_name(name: Optional[str] = None, test: int) this will throw error as name is optional parameter
# to fix this we can place * as first parameter which denotes required parameter and rest all parameters are optional
# def get_by_name(*, name: Optional[str] = None, test: int)


# Combining Path and Query parameters

@app.get("/student_by_intake/{student_id}")
def get_intake(*, student_id: int, intake:Optional[str]=None):
    for student_id in students:
        if students[student_id]["intake"] == intake:
            return students[student_id]
    return {"Data":"Not found"}


# Request body and post methods
# used to include new object in database
@app.post("/create_student/{student_id}")
def create_new_student(student_id: int, student: stdent):
    if student_id in students:
        return {"Error": "Student already exists"}
    
    students[student_id] = student
    return students[student_id]


# put method - to update the data
@app.put("/update_student{student_id}")
def update_student_details(student_id: int, student: update_student):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    
    # students[student_id] = student
    # return student

    # above commented code will assign null to the unchanged attributes of class i.e. if user wants to change only name then age and intake will be assigned as null
    # to handle this we will make below modifications

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.intake != None:
        students[student_id].intake = student.intake

    return students[student_id]

# delete student id
@app.delete("/delete_student{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    
    del students[student_id]
    
    return students
    # return {"Message":"Student deleted successfully"}


