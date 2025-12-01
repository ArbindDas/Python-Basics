class Parent:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.address = ""
        print(" parent Default constructor called.....")

    def greet(self):
        print("i am parent")




class Grandpa:

    def __init__(self):
        super().__init__ #MRO ->  Method Resolution Orde
        print("i am grandpa constuctor")


    def gretting(self):
        print("i am from grandpa")


class Child(Parent , Grandpa):

    def __init__(self):
        super().__init__()  #MRO ->  Method Resolution Orde
        print("i am child constructor.....")




child = Child()

child.greet();
child.gretting();
