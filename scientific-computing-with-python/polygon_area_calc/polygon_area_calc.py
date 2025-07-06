# Define the Rectangle class
class Rectangle:
    # Constructor method: initializes a new rectangle with width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    # Method to set the width
    def set_width(self, width):
        self.width = width

    # Method to set the height
    def set_height(self, height):
        self.height = height
        
    # Returns the area of the rectangle (width * height)
    def get_area(self):
        return self.width * self.height
    
    # Returns the perimeter: 2 * (width + height)
    def get_perimeter(self):
        return self.width * 2 + self.height * 2
    
    # Returns the diagonal using the Pythagorean theorem
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    # Returns a string representation of the shape made with "*"
    def get_picture(self):
        # Prevents creating huge pictures for large rectangles
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            picture = ''
            # Builds each line with '*' repeated width times, for height lines
            for _ in range(self.height):
                picture += "*" * self.width + "\n"
            return picture
        
    # Calculates how many times another shape can fit inside this one
    def get_amount_inside(self, shape):
        # Uses integer division to ensure full fit, no partial shapes
        fits_width = self.width // shape.width
        fits_height = self.height // shape.height
        return fits_width * fits_height
    
    # String representation of the object for printing
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
            

# Define the Square class, which inherits from Rectangle
class Square(Rectangle):
    # Constructor method: only takes one side since all sides are equal
    def __init__(self, side):
        # Initializes width and height to the same value using Rectangle's constructor
        super().__init__(side, side)
    
    # Sets both width and height to the same side length
    def set_side(self, side):
        self.width = side
        self.height = side
        
    # Overrides set_width to ensure both width and height stay equal
    def set_width(self, width):
        self.width = width
        self.height = width
        
    # Overrides set_height to ensure both width and height stay equal
    def set_height(self, height):
        self.width = height
        self.height = height
        
    # String representation of a Square
    def __str__(self):
        return f"Square(side={self.width})"
