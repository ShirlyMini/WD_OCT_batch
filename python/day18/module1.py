def add(n1,n2):
    print("add ",n1+n2)

def multiply(n1,n2):
    print("multiply",n1*n2)

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
    print(f"from class A __name__:{__name__}")
    def display(self):
        print(f"from class A dispaly method __name__:{__name__}")
        print("this is class A")

obj=A()
obj.display()
print(f"from module1 __name__:{__name__}")#from module1 __main__