from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):  # ABC is the parent class

    @abstractmethod
    def speak(self):
        pass

    def sleep(self):
        print("Animal is sleeping")


# Concrete subclass
class Dog(Animal):
    def speak(self):
        print("Dog barks")


dog = Dog()
dog.speak()  # Dog barks
dog.sleep()  # Animal is sleeping
