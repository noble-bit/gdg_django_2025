import os
import json

class Todo:
    def __init__(self, title, task_id, completed=False):
        
        self.id = task_id
        self.completed = completed
        self.title = title

    def to_dict(self):
        
        return {
            "id": self.id,
            "completed": self.completed,
            "title": self.title
        }
    
class TodoApp:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = []
        self.load_todos()

    def load_todos(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                for item in data:
                    self.todos.append(
                        Todo(item["id"],item["completed"],item["title"])
                    )

    def save_todos(self):
        with open(self.filename, "w") as f:
            json.dump(
                [todo.to_dict() for todo in self.todos],
                f,
                indent = 4
            )
    