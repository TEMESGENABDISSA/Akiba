class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Department: {self.department}")

    def introduce(self):
        print(f"Hi, I am {self.name}. I study {self.department}.")


s1 = Student("Abel", "S001", "Computer Science")
s2 = Student("Sara", "S002", "Engineering")
s3 = Student("Temesgen", "S003", "Business")

for s in [s1, s2, s3]:
    s.display_info()
    s.introduce()
    print("-" * 25)
   
# Answers

# 1  What is a class in Python?
# A class is a blueprint for making objects. It describes the data the objects
# will have (attributes) and the things they can do (methods)
# Example: Student is the blueprint for all students.

# 2 What is an object?
# An object is a real thing made from a class. It has its own data.
# Example s1 is a real student named Abel. One class can make many objects,
# like s1, s2 and s3

# 3 What is the purpose of the __init__() method?
# It is the constructor. It runs automatically when an object is created and
# sets the starting values of the attributes.
# Example: Student("Abel", "S001", "Computer Science") saves the name, id and
# department inside the new object.

# 4 What is the difference between an attribute and a method?
# An attribute is data that belongs to an object, like name or student_id
# A method is a function inside a class that does an action, like
# display_info() or introduce()
# In short, an attribute is what the object has, and a method is what the
# object can do