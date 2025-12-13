class Car:
    
    def __init__(self,make):
        self.make = make
    
    def get_method(self):
        return self.make


car1 = Car('Hello')
print(car1.get_method())

