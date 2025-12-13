class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def annual_salary(self):
        return self.salary * 12


emp = Employee("Nebil", 5000)
print(f"{emp.name}'s monthly salary: {emp.salary}")
print(f"{emp.name}'s annual salary: {emp.annual_salary()}")

