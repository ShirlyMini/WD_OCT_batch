# a,b=10,20# global
# class myclass:
#     a,b=100,200 # class variable
#     def myfunc1(self): #
#         print(self) # obj
#         print(myclass)# classname
#         a,b=1,2 # local variable
#         print(f"local variable {a} {b}")
#         print(f"class variable {self.a} {self.b}")
#         print(f"class variable {myclass.a} {myclass.b}")
#         print(globals())
#         print(f"global variable {globals()['a']} {globals()['b']}")
#
#     @classmethod
#     def myfunc2(cls): #
#         print(cls) # classname
#         print(myclass)# classname
#         a,b=1,2 # local variable
#         print(f"local variable {a} {b}")
#         print(f"class variable {cls.a} {cls.b}")
#         print(f"class variable {myclass.a} {myclass.b}")
#         print(globals())
#         print(f"global variable {globals()['a']} {globals()['b']}")
#
#     @staticmethod
#     def myfunc3(): #
#         print(myclass)
#         a,b=1,2 # local variable
#         print(f"local variable {a} {b}")
#         # print(f"class variable {cls.a} {cls.b}") # invalid
#         print(f"class variable {myclass.a} {myclass.b}")
#         print(globals())
#         print(f"global variable {globals()['a']} {globals()['b']}")
#
# obj=myclass()
# #myclass.myfunc1()
# obj.myfunc1()
#
# #obj.myfunc2()
# obj.myfunc3()


# instance var vs class var vs local vs global var

# a="global variable"
#
# class myclass:
#     a="class variable"
#
#     def __init__(self):
#         a="instance variable"
#
#         print(f"global variable a={globals()['a']}")
#         print(f"class variable a={myclass.a}")
#         print(f"instance variable a={a}")
#         print(f"instance variable self.a={self.a}")
#         self.a = a
#
#         print(f"global variable a={globals()['a']}")
#         print(f"class variable a={myclass.a}")
#         print(f"instance variable a={a}")
#         print(f"instance variable self.a={self.a}")
#
#     def myfunc1(self):
#         print(f"global variable a={globals()['a']}")
#         print(f"class variable a={myclass.a}")
#         print(f"instance variable a={a}")
#         print(f"instance variable self.a={self.a}")
#
#     @classmethod
#     def myfunc2(self):
#         print(f"global variable a={globals()['a']}")
#         print(f"class variable a={myclass.a}")
#         print(f"instance variable a={a}")
#         print(f"instance variable self.a={self.a}") # cannot access instance variable in classmethod
#
#     @staticmethod
#     def myfunc3():
#         print(f"global variable a={globals()['a']}")
#         print(f"class variable a={myclass.a}")
#         print(f"instance variable a={a}")
#         #print(f"instance variable self.a={self.a}")
#
# obj=myclass()
# #obj.myfunc1()
# # obj.myfunc2()
# obj.myfunc3()


a="global variable"
#
class myclass:
    """this my class"""

    a="class variable"

    def __init__(self):
        a="instance variable"

        print(f"global variable a={globals()['a']}")
        print(f"class variable a={myclass.a}")
        print(f"instance variable a={a}")
        print(f"instance variable self.a={self.a}")
        #self.a = a
        myclass.a = a

        print(f"global variable a={globals()['a']}")
        print(f"class variable a={myclass.a}")
        print(f"instance variable a={a}")
        print(f"instance variable self.a={self.a}")

    def myfunc1(self):
        print(f"global variable a={globals()['a']}")
        print(f"class variable a={myclass.a}")
        print(f"instance variable a={a}")
        print(f"instance variable self.a={self.a}")

    @classmethod
    def myfunc2(cls):
        print(f"global variable a={globals()['a']}")
        print(f"class variable a={myclass.a}")
        print(f"instance variable a={a}")
        print(f"instance variable self.a={cls.a}") # cannot access instance variable in classmethod

    @staticmethod
    def myfunc3():
        print(f"global variable a={globals()['a']}")
        print(f"class variable a={myclass.a}")
        print(f"instance variable a={a}")
        #print(f"instance variable self.a={self.a}")

obj=myclass()
obj.myfunc1()
obj.myfunc2()
obj.myfunc3()

print(dir(myclass))

print(myclass.__doc__)