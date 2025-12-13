class Rectangle:
   
    def __init__(self,height,width):
        self.width = width
        self.height = height
    
    def area(self):
        return self.height * self.width

rec = Rectangle(15, 35)
print(rec.area())

