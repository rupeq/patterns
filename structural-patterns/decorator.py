from abc import ABC, abstractmethod

# Component
class IShape(ABC):
    @abstractmethod
    def show_info(self):
        pass
    
# Object
class Square(IShape):
    def show_info(self):
        print("square")
        
# Decorator: create an object
class ShapeDecorator(IShape):
    def __init__(self, shape):
        self.shape = shape
        
    # Operation()
    def show_info(self):
        self.shape.show_info()
        
# Decorator: color
class ColorShape(ShapeDecorator):
    def __init__(self, shape, color):
        super().__init__(shape)
        self.color = color
        
    def show_info(self):
        print(self.color + "")
        self.shape.show_info()
        
# Decorator: shadow
class ShadowShape(ShapeDecorator):
    def show_info(self):
        self.shape.show_info()
        print("with shadow")
        
# Client
square = Square()
square.show_info() # printed: square

colorShape = ColorShape(square, "red")
colorShape.show_info() # printed: red square

shadowShape = ShadowShape(colorShape)
shadowShape.show_info() # printed: red squere with shadow
