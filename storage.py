import json
import os

TODOS_FILE="data/todos.json"
STUDENTS_FILE="data/students.json"
PRODUCTS_FILE="data/products.json"

def read_data(filepath:str)->list:
    "Read all items from a JSON file. Return empty list if file doesnt exist."
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r")as f:
        return json.load(f)
    
def write_data(filepath: str , data: list)->None:
    "Write all items to a JSON file."
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath,"w") as f:
        json.dump(data, f, indent=2)
        
def generate_id(items: list)->int:
    "Generate a new unique ID that is never reused even after deletetion."
    if items:
        return max(item["id"] for item in items)+1
    return 1
