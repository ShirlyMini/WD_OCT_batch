# variables in class
# local vs global vs class variable
# a,b=10,20# global
# class myclass:
#     x,y=100,200 # class variable
#     def myfunc1(self): #
#         i,j=1,2 # local variable
#         print(f"local variable {i} {j}")
#         print(f"class variable {self.x} {self.y}")
#         print(f"class variable {myclass.x} {myclass.y}")
#         print(f"global variable {a} {b}")
#
# obj=myclass()
# obj.myfunc1()

# a,b=10,20# global
# class myclass:
#     a,b=100,200 # class variable
#     def myfunc1(self): #
#         a,b=1,2 # local variable
#         print(f"local variable {a} {b}")
#         print(f"class variable {self.a} {self.b}")
#         print(f"class variable {myclass.a} {myclass.b}")
#         print(globals())
#         print(f"global variable {globals()['a']} {globals()['b']}")
#
#     @classmethod
#     def myfunc2(cls): #
#         a,b=1,2 # local variable
#         print(f"local variable {a} {b}")
#         print(f"class variable {cls.a} {cls.b}")
#         print(f"class variable {myclass.a} {myclass.b}")
#         print(globals())
#         print(f"global variable {globals()['a']} {globals()['b']}")
#
#     @staticmethod
#     def myfunc3(): #
#         a,b=1,2 # local variable
#         print(f"local variable {a} {b}")
#         # print(f"class variable {cls.a} {cls.b}") # invalid
#         print(f"class variable {myclass.a} {myclass.b}")
#         print(globals())
#         print(f"global variable {globals()['a']} {globals()['b']}")
#
# obj=myclass()
# obj.myfunc1()
# obj.myfunc2()
# obj.myfunc3()


a,b=10,20# global
class myclass:
    a,b=100,200 # class variable
    def myfunc1(self, a,b): ## a and b local variable
        # print(self)
        # print(myclass)
        print(f"local variable {a} {b}")
        print(f"class variable {self.a} {self.b}")
        print(f"class variable {myclass.a} {myclass.b}")
        print(globals())
        print(f"global variable {globals()['a']} {globals()['b']}")

    @classmethod
    def myfunc2(cls,a,b): ## a and b local variable
        # print(cls)
        # print(myclass)
        print(f"local variable {a} {b}")
        print(f"class variable {cls.a} {cls.b}")
        print(f"class variable {myclass.a} {myclass.b}")
        print(globals())
        print(f"global variable {globals()['a']} {globals()['b']}")

    @staticmethod
    def myfunc3(a,b): ## a and b local variable
        print(f"local variable {a} {b}")
        # print(f"class variable {cls.a} {cls.b}") # invalid
        print(f"class variable {myclass.a} {myclass.b}")
        print(globals())
        print(f"global variable {globals()['a']} {globals()['b']}")

obj=myclass()
obj.myfunc1(1,2)
obj.myfunc2(3,4)
obj.myfunc3(5,6)
