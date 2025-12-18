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
    
    def add(self, title):
        task_id = len(self.todos) + 1
        self.todos.append(Todo(task_id, title))
        self.save_todos()
    
    def view_tasks(self):
        if not self.todos:
            print("No tasks.")
            return

        for todo in self.todos:
            status = "Done" if todo.completed else "Not Done"
            print(f"{todo.id}. {todo.title} - {status}")

    def complete_todo(self, task_id):
        for todo in self.todos:
            if todo.id == task_id:
                todo.completed = True
                self.save_todos()
                return
        print("Task not found.")

        
    def delete(self, task_id):
        self.todos = [todo for todo in self.todos if todo.id != task_id]
        self.save_todos()



        