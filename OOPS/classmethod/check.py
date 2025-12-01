class Employee:
    company_name = "ABC Corp"  # class variable

    def __init__(self, name, salary):
        self.name = name       # instance variable
        self.salary = salary   # instance variable

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company  # modify class variable

    @classmethod
    def from_string(cls, emp_str):
        # Alternative constructor using string
        name, salary = emp_str.split("-")
        return cls(name, int(salary))

# Using class methods
Employee.change_company("XYZ Corp")
print(Employee.company_name)  # XYZ Corp

emp1 = Employee.from_string("Arbind-50000")
print(emp1.name, emp1.salary, Employee.company_name)
