
# Task 1 Student Information System
class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print("Name", self.name)
        print("Age", self.age)
        print("Department", self.department)
        print()


# Create three students
student1 = Student("Abel", 20, "Computer Science")
student2 = Student("Selam", 22, "Software Engineering")
student3 = Student("Daniel", 19, "Information Systems")

# Show the information of each student
student1.display_info()
student2.display_info()
student3.display_info()




# Task 2: Rectangle Calculator

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create rectangles
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
# Show the area and perimeter of each rectangle
print("Rectangle 1")
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())
print()

print("Rectangle 2")
print("Area", rect2.area())
print("Perimeter", rect2.perimeter())