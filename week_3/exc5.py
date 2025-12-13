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
        
