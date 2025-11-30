class GrandFather:
    def __init__(self, id=0, name="", address=""):
        self.id = id
        self.name = name
        self.address = address
        print("GrandFather constructor called")

    def greet_grandfather(self):
        print("Hello my sons, I am your papa")


class Father(GrandFather):
    def __init__(self, id=0, name="", address="", salary=0):
        super().__init__(id, name, address)
        self.salary = salary
        print("Father constructor called")

    def greet_father(self):
        print("I am from Father class, you are my son")


class Child(Father):
    def __init__(self, id=0, name="", address="", salary=0, school=""):
        super().__init__(id, name, address, salary)
        self.school = school
        print("Child constructor called")

    def greet_child(self):
        print("I am from Child class")


# ====== Usage Example ======

# Create a child object with all details
c = Child(id=101, name="Arbind", address="Jeetpur", salary=50000, school="ABC School")

# Access all properties and methods
print(f"ID: {c.id}, Name: {c.name}, Address: {c.address}, Salary: {c.salary}, School: {c.school}")
c.greet_grandfather()  # GrandFather method
c.greet_father()       # Father method
c.greet_child()        # Child method
