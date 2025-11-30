

class Calculator:
    def __init__(self):
        print("Calculator constructor called....")



    def add(self , *args):
        return sum(args)
    

    def addtwo(self , a , b = 0 , c = 0):
        return a + b + c



cal = Calculator()
print(cal.add(5, 10))
print(cal.add(5, 10 , 10))
