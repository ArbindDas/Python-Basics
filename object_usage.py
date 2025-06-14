class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def info(self):
        return f"{self.model} - {self.year}"

c1 = Car("Toyota", 2020)
c2 = Car("Honda", 2022)
print(c1.info())
print(c2.info())