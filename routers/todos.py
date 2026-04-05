from fastapi import APIRouter, HTTPException
from datetime import datetime
from models import Todo,TodoUpdate
from storage import read_data, write_data, generate_id, TODOS_FILE

router= APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

@router.get("/")
def get_todos():
    return read_data(TODOS_FILE)

@router.get("/{todo_id}")
def get_todo(todo_id:int):
    todos= read_data(TODOS_FILE)
    for todo in todos:
        if todo["id"]==todo_id:
            return todo
    raise HTTPException(
        status_code=404,
        detail=f"Todo with id {todo_id} not found"
    )

@router.post("/")
def create_todo(todo : Todo):
    todos= read_data(TODOS_FILE)
    new_todo = {
        "id": generate_id(todos),
        "title": todo.title,
        "description": todo.description,
        "category": todo.category,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    todos.append(new_todo)
    write_data(TODOS_FILE, todos)
    return new_todo

@router.put("/{todo_id}")
def update_todo(todo_id: int ,updated: TodoUpdate):
    todos=read_data(TODOS_FILE)
    for todo in todos:
        if todo['id']==todo_id:
            if updated.title is not None:
                todo["title"]=updated.title
            if updated.description is not None:
                todo["description"]=updated.description
            if updated.category is not None:
                todo["category"]=updated.category
            todo["updated_at"]=datetime.now().isoformat()
            write_data(TODOS_FILE , todos)
            return todo
    raise HTTPException(status_code=404 , detail= f" Todo with id {todo_id} not found")

@router.delete("/{todo_id}")
def delete_todo(todo_id:int):
    todos = read_data(TODOS_FILE)
    for todo in todos:
        if todo["id"]== todo_id:
            todos.remove(todo)
            write_data(TODOS_FILE, todos)
            return {
                "message": f"Todo '{todo['title']}' deleted successfully"
            }
    raise HTTPException(status_code=404 ,detail=f"Todo with id {todo_id} not found")