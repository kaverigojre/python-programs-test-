import math

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b==0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    def square_root(self, x):
        return math.sqrt(x)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    
    #Implement the feature to calculate the area of a rectangle
    def calculate_rectangle_area(self, length, width):
        return length * width


      #Implement the feature to calculate the area of a rectangle

        def calculate_rectangle_area(self, length, width):
            return length * width
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
    # Implement the feature to calculate the area of a circle
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2


<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

if __name__ == "__main__":
    calculator = Calculator()
    num1 = 16
    num2 = 4
    num3= 25
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    length = 10
    width = 6
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
=======
    radius = 5

>>>>>>> Stashed changes
=======
    radius = 5

>>>>>>> Stashed changes
=======
    radius = 5

>>>>>>> Stashed changes
    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
    print(f"The square root of {num3} = {calculator.square_root(num3)}")

<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    #Implement the feature to calculate the area of a rectangle
    print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")
=======
    print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")   #Implement the feature to calculate the area of a rectangle
>>>>>>> Stashed changes
=======
     # Implement the feature to calculate the area of a circle
    print(f"The area of the circle with radius {radius} ={calculator.calculate_circle_area(radius)}")
>>>>>>> Stashed changes
=======
     # Implement the feature to calculate the area of a circle
    print(f"The area of the circle with radius {radius} ={calculator.calculate_circle_area(radius)}")
>>>>>>> Stashed changes
=======
     # Implement the feature to calculate the area of a circle
    print(f"The area of the circle with radius {radius} ={calculator.calculate_circle_area(radius)}")
>>>>>>> Stashed changes
