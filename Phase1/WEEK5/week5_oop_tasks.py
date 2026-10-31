
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