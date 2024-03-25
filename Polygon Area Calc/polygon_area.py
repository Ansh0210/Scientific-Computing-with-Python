class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, amount):
        self.width = amount
    
    def set_height(self, amount):
        self.height = amount
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        s = ""
        
        if self.height > 50 or self.width > 50:
            s = "Too big for picture."
            return s
            
        for i in range(self.height):
            s += f"{self.width * '*'}\n"
            
        return s
    
    def get_amount_inside(self, shape):
        amt_inside = self.get_area()//shape.get_area()
        return amt_inside
    
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        #self.length = length
    
    def __str__(self):
        return f"Square(side={self.height})"
    
    def set_side(self, amount):
        self.height = amount
        self.width = amount
    
    def set_width(self, amount):
        self.width = amount
        self.height = amount
    
    def set_height(self, amount):
        self.height = amount
        self.width = amount
    
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
rect.set_width(5)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(5)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))