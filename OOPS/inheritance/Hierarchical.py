# Parent class
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        print("Employee constructor called")

    def greet(self):
        print(f"Hello, I am {self.name}, Employee ID: {self.id}")


# First child class
class Manager(Employee):
    def __init__(self, id, name, department):
        super().__init__(id, name)
        self.department = department
        print("Manager constructor called")

    def display_department(self):
        print(f"Manager of department: {self.department}")


# Second child class
class Developer(Employee):
    def __init__(self, id, name, language):
        super().__init__(id, name)
        self.language = language
        print("Developer constructor called")

    def display_language(self):
        print(f"Developer knows: {self.language}")


# ====== Usage ======

m = Manager(1, "Arbind", "HR")
m.greet()                 # Parent method
m.display_department()    # Child method

d = Developer(2, "Rohit", "Python")
d.greet()                 # Parent method
d.display_language()      # Child method
