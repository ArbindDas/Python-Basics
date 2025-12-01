# Parent class
class Employee:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.address = ""

    def grettings(self):
        print("I am parent")

    @classmethod
    def with_details(cls, id, name, address):
        obj = cls()
        obj.id = id
        obj.name = name
        obj.address = address
        return obj

    def printDetails(self):
        print("id:", self.id)
        print("name:", self.name)
        print("address:", self.address)


# Child class inheriting from Employee
class Child(Employee):

    def __init__(self):
        super().__init__()  # ✅ call Parent constructor
        print("Child constructor called")

    def greet(self):
        print("I am from child, single inheritance...")


# Grandchild class inheriting from Child
class Manager(Child):

    def __init__(self):
        super().__init__()  # ✅ call Child constructor (which calls Employee constructor)
        print("Manager constructor called")

    def manager_info(self):
        print("I am a Manager, multilevel inheritance example")


# Testing multilevel inheritance
mgr = Manager()

mgr.id = 101
mgr.name = "Arbind"
mgr.address = "Jeetpur"

mgr.printDetails()   # inherited from Employee
mgr.grettings()      # inherited from Employee
mgr.greet()          # inherited from Child
mgr.manager_info()   # own method
