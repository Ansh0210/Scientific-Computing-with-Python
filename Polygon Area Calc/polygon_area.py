class Rectangle:
    def __init__(self, width, height):
        # Initialize a rectangle with the given width and height
        self.width = width
        self.height = height

    def __str__(self):
        # Provide a string representation of the rectangle
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, amount):
        # Set the width of the rectangle to a new value
        self.width = amount
    
    def set_height(self, amount):
        # Set the height of the rectangle to a new value
        self.height = amount
    
    def get_area(self):
        # Calculate and return the area of the rectangle
        return self.width * self.height
    
    def get_perimeter(self):
        # Calculate and return the perimeter of the rectangle
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        # Calculate and return the length of the rectangle's diagonal
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        # Return a string that represents a picture of the rectangle using asterisks
        # If the rectangle's dimensions are too large, return an error message
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
            
        picture = ""
        for i in range(self.height):
            picture += f"{self.width * '*'}\n"
            
        return picture
    
    def get_amount_inside(self, shape):
        # Calculate and return the number of times the given shape can fit inside the rectangle
        # without overlapping, based on their areas
        return self.get_area() // shape.get_area()
    
class Square(Rectangle):
    def __init__(self, side):
        # Initialize a square by using the Rectangle class, setting both width and height to the side length
        super().__init__(side, side)
    
    def __str__(self):
        # Provide a string representation of the square
        return f"Square(side={self.height})"
    
    def set_side(self, amount):
        # Set all sides of the square to a new value
        self.width = self.height = amount
    
    def set_width(self, amount):
        # Override to set both the width and height when width is set, maintaining the square's property
        self.set_side(amount)
    
    def set_height(self, amount):
        # Override to set both the width and height when height is set, maintaining the square's property
        self.set_side(amount)

    
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