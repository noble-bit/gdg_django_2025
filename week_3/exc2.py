class Dog:
    def __init__(self,sound):
        self.sound = sound
    
    def bark(self):
        return self.sound

dog = Dog("woof!")
print(dog.bark())
