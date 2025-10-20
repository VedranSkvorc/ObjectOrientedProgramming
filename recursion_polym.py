#recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

#polymorphism
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return "Calculating circle area"

class Square(Shape):
    def area(self):
        return "Calculating square area"

for shape in [Circle(), Square()]:
    print(shape.area())
