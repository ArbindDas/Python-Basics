# Class definition for Employee
class Employee:
    # Constructor method to initialize object properties
    def __init__(self, name, salary):
        self.__name = name       # Private variable: hides the name from direct access
        self.__salary = salary   # Private variable: hides the salary from direct access

    # Getter method for name
    def get_name(self):
        return self.__name       # Provides controlled access to private variable __name

    # Getter method for salary
    def get_salary(self):
        return self.__salary     # Provides controlled access to private variable __salary

    # Setter method for name
    def set_name(self, name):
        self.__name = name       # Allows updating private variable __name safely

    # Setter method for salary
    def set_salary(self, salary):
        if salary > 0:           # Validate input before updating
            self.__salary = salary
        else:
            print("invalid salary...")  # Prevents invalid/negative salary assignment

# Creating an Employee object
emp = Employee("Arbind", 900000)  # Calls __init__, initializes __name and __salary

# Updating the name using setter
emp.set_name("Jai")                # Encapsulation: modifies private variable safely

# Accessing name using getter
print(emp.get_name())              # Prints updated name using controlled access
