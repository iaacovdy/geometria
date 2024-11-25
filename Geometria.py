class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, *args):
        if len(args) == 3:  
            # Metodo 1: Esquina inf izq + ancho y alto
            self.bottom_left = args[0]
            self.width = args[1]
            self.height = args[2]
        elif len(args) == 2 and isinstance(args[0], Point):  
            # Metodo 2: Centro + ancho y alto
            self.center = args[0]
            self.width = args[1]
            self.height = args[2]
            self.bottom_left = Point(self.center.x - self.width / 2, self.center.y - self.height / 2)
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):  
            # Metodo 3: Esquinas opuestas
            self.bottom_left = args[0]
            self.upper_right = args[1]
            self.width = self.upper_right.x - self.bottom_left.x
            self.height = self.upper_right.y - self.bottom_left.y
        else:
            raise ValueError("Valores invalidos")
        
        # Centro para dos esquinas
        if hasattr(self, 'infizq') and hasattr(self, 'supder'):
            self.center = Point(
                (self.bottom_left.x + self.upper_right.x) / 2,
                (self.bottom_left.y + self.upper_right.y) / 2
            )
        
    def compute_area(self):
        return self.width * self.height
    
    def compute_perimeter(self):
        return 2 * (self.width + self.height)

    def compute_interference_point(self, point):
        # Determina si el punto está dentro del rectángulo
        if (self.bottom_left.x <= point.x <= self.bottom_left.x + self.width and
            self.bottom_left.y <= point.y <= self.bottom_left.y + self.height):
            return True
        return False

class Square(Rectangle):
    def __init__(self, *args):
        if len(args) == 3:
            # Si alto=ancho para método 1
            if args[1] != args[2]:
                raise ValueError("El ancho y alto deben ser iguales para formar un cuadrado")
            super().__init__(args[0], args[1], args[2])
        elif len(args) == 2 and isinstance(args[0], Point):
            # Si alto=ancho para método 2
            super().__init__(args[0], args[1], args[1])
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point): 
            # Si diferencia en x es igual a diferencia y métido 3
            if args[1].x - args[0].x != args[1].y - args[0].y:
                raise ValueError("El ancho y alto deben ser iguales para formar un cuadrado")
            super().__init__(args[0], args[1])
        else:
            raise ValueError("Valores invalidos")

# Metodo 1:
bl_point = Point(0, 0)
rect = Rectangle(bl_point, 4, 5)

# Metodo 2:
center_point = Point(2, 2)
rect_center = Rectangle(center_point, 4, 6)

# Metodo 3:
bl_point_2 = Point(0, 0)
ur_point = Point(4, 6)
rect_corners = Rectangle(bl_point_2, ur_point)

# Dimensiones cuadrado
square_point = Point(2, 2)
square = Square(square_point, 4)

# Area y perímetro
print(f"Area rectangulo: {rect.compute_area()}")
print(f"Perimetro rectangulo: {rect.compute_perimeter()}")

# Punto dentro del área
point_inside = Point(2, 3)
point_outside = Point(5, 6)
print(f"Dentro: {rect.compute_interference_point(point_inside)}")
print(f"Fuera: {rect.compute_interference_point(point_outside)}")
