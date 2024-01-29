# 3types
# instance method (self)(default)
# static method
# class method

class myclass:
    def myfunc1(self):
        print(self)
        print("printing myfunc1")

    def myfunc2(self, a,b):
        return a+b

    @staticmethod
    def myfunc3():
        print("printing myfunc3")

    @staticmethod
    def myfunc4(a,b):
        print(f"printing {a+b}")

    @classmethod
    def myfunc5(cls):
        print(cls)
        print("printing myfunc5")

    @classmethod
    def myfunc6(cls, a,b):
        print(f"printing {a+b}")

# obj=myclass() # object or instance creation
# print(obj)
# obj.myfunc1()
# # class name will get passed as first parameter in the backend
# print(obj.myfunc2(10,20))


# instance method
myclass().myfunc1() #printing myfunc1
# #myclass.myfunc1() #TypeError: myclass.myfunc1() missing 1 required positional argument: 'self'
#

# static method
myclass().myfunc3()
myclass.myfunc3() # staticmethod no object creation


# myclass().myfunc4(1,2)
# myclass.myfunc4(3,4)

# class method
myclass().myfunc5()
#class name will get passed as first parameter in the backend
myclass.myfunc5()
myclass.myfunc6(1,2)