from pydantic import BaseModel
from typing import Optional

#=======================
#todo model
#=======================

class Todo(BaseModel):
    title: str
    description: str
    category: str

class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    category: Optional[str]


#======================
#student model
#======================

class Student(BaseModel):
    name: str
    age: int
    grade: str

class StudentUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    grade: Optional[str]

#======================
#product model
#======================

class Product(BaseModel):
    name: str
    price: float
    category: str
    stock: int

class ProductUpdate(BaseModel):
    name: Optional[str]
    price: Optional[float]
    category: Optional[str]
    stock: Optional[int]

