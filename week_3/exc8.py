class Animal:
    def make_sound(self):
        return "animal sound"

class Cat(Animal):  
    def make_sound(self):
        return "Meow"


animal = Animal()
cat = Cat()

print("Animal sound:", animal.make_sound())  
print("Cat sound:", cat.make_sound())        