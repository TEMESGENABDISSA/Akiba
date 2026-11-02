
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

#  Student Score Management

class Student:
    # Class attribute shared by ALL students
    school_name = "Akiba Academy"

    def __init__(self, name, score, department):
        # Instance attributes different for each student
        self.name = name
        self.score = score
        self.department = department

    def display(self):
        print("School:", Student.school_name)
        print("Name:", self.name)
        print("Score:", self.score)
        print("Department:", self.department)
        print()


# Create three students
student1 = Student("Abel", 85, "Computer Science")
student2 = Student("Selam", 90, "Software Engineering")
student3 = Student("Daniel", 70, "Information Systems")

# Update the score of one student
student1.score = 95

# Display all students only Abel's score changed
student1.display()
student2.display()
student3.display()

# Answers
# 1 A class attribute (school_name) belongs to the class and is shared by all
#    objects. If it changes, every student sees the change An instance
#    attribute (name, score, department) belongs to one object only, so each
#    student has their own value
#
# 2 Each student object stores its own score. When we write student1.score = 95,
#    only student1's score changes student2 and student3 are separate objects
#    in memory, so their scores stay the same




# Task 4: Product Information System

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price} birr, Quantity: {self.quantity}"

    def total_value(self):
        return self.price * self.quantity

product1 = Product("Laptop", 45000, 3)
product2 = Product("Phone", 15000, 5)
product3 = Product("Notebook", 50, 100)

# Print each object directly
print(product1)
print(product2)
print(product3)
print()

print("Laptop total value:", product1.total_value())
print("Phone total value:", product2.total_value())
print("Notebook total value:", product3.total_value())
print()

# Answer:
# The __str__() method tells Python how to turn an object into readable text.
# Without it, print(product1) shows something unreadable like
# <__main__.Product object at 0x000001>. With it, print() shows the product's
# name, price and quantity in a clear sentence.