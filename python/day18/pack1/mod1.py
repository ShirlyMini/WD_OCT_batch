def display():
    print("func display in mod1")

class bird:
    var1=100

    def __init__(self, a,b):
        self.a=a
        self.b=b
        print("constrctor ")

    def display(self):
        print("this is parrot")

    @classmethod
    def show1(cls):
        print("this is parrot, class method")

    @staticmethod
    def show2():
        print("this is parrot, static method")

class A:
    def display(self):
        print("this is class A")