class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def info(self):
        return f"Vehicle: {self.brand}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)  
        self.model = model
    
    def info(self):  
        return f"Car: {self.brand} {self.model}, Year: {self.year}"


vehicle = Vehicle("Toyota", 2020)
car = Car("Toyota", 2022, "Camry")

print(vehicle.info())  
print(car.info())     