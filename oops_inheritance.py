class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

a = Animal()
d = Dog()
print(a.sound())
print(d.sound())