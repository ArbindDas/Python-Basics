
class Test:

    def __init__(self):
        print("Test constructor called.....")
    

    def test(self):
        print("Testing api.....")



class Developer:

    def __init__(self):
        print("Developer constructor called....")

    
    def test(self):
        print("the Redis port are sucessfully working....")


class Tester:

    def __init__(self):
        print("Tester constructor called.....")

    def test(self):
        print("Tester test his endpoints securely....")



#using ploymorphism

objs = [Test(), Developer(), Tester()]



for obj in objs:
    obj.test()    # same method name, different behavior