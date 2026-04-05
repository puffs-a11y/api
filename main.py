from fastapi import FastAPI
from routers import todos,students, product

app=FastAPI(
    title="CRUD API",
    description="A simple API for managing Todos, Students and Products"
)

app.include_router(todos.router)
app.include_router(students.router)
app.include_router(product.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to the serverrr!",
        "docs": "Visit /docs to explore all endpoints :)"
    }