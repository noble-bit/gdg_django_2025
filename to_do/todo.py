import os
import json

class Todo:
    
    def __init__(self, task_id, title, completed=False):
            self.id = task_id
            self.title = title
            self.completed = completed

    def to_dict(self):
        
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            
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
                        Todo(item["id"], item["title"], item["completed"])
                    )

    def save_todos(self):
        with open(self.filename, "w") as f:
            json.dump([todo.to_dict() for todo in self.todos], f, indent=4)

    def add_todo(self, title):
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

    def delete_todo(self, task_id):
        self.todos = [todo for todo in self.todos if todo.id != task_id]
        self.save_todos()

my_todo_app = TodoApp()

while True:
    print("\n1. Add Todo")
    print("2. View Todos")
    print("3. Mark as Completed")
    print("4. Delete Todo")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Enter task title: ")
        my_todo_app.add_todo(title)

    elif choice == "2":
        my_todo_app.view_tasks()

    elif choice == "3":
        task_id = int(input("Enter task ID: "))
        my_todo_app.complete_todo(task_id)

    elif choice == "4":
        task_id = int(input("Enter task ID: "))
        my_todo_app.delete_todo(task_id)

    elif choice == "5":
        break

    else:
        print("Invalid choice")


        