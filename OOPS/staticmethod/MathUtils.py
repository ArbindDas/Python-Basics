class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def isHighSalary(salary):
        return salary > 5000

# Calling static methods without creating an object
print(MathUtils.add(5, 10))       # 15
print(MathUtils.multiply(5, 10))  # 50


print(MathUtils.isHighSalary(100000))
