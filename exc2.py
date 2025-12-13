# class Person:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


# p1 = Person("Nebil","75")

# print(p1.name,'is',p1.age,'years old')

# class Dog:
#     def __init__(self,sound):
#         self.sound = sound
    
#     def bark(self):
#         return self.sound



# dog = Dog("woof!")
# print(dog.bark())

# class Car:
    
#     def __init__(self,make):
#         self.make = make
    
#     def get_method(self):
#         return self.make


# car1 = Car('Hello')
# print(car1.get_method())

# class Rectangle:
   
#     def __init__(self,height,width):
#         self.width = width
#         self.height = height
    
#     def area(self):
#         return self.height * self.width

# rec = Rectangle(15, 35)
# print(rec.area())

class Student:
    def __init__(self):
        self.__grade = None  
    
    def set_grade(self, grade):
        self.__grade = grade
    
    def get_grade(self):
        return self.__grade


student = Student()

student.set_grade(85)
print(student.get_grade())  

student.set_grade(90)
print(student.get_grade())  
        
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def annual_salary(self):
        return self.salary * 12


emp = Employee("Nebil", 5000)
print(f"{emp.name}'s monthly salary: {emp.salary}")
print(f"{emp.name}'s annual salary: {emp.annual_salary()}")

class Library:
    def __init__(self):
        self.books = []  
    
    def add_book(self, book_title):
        self.books.append(book_title)
        print(f"Added: {book_title}")
    
    def show_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")


lib = Library()


lib.add_book("Book1")
lib.add_book("Book2")
lib.add_book("Book3")


print()  
lib.show_books()


print("\n--- Testing empty library ---")
empty_lib = Library()
empty_lib.show_books()