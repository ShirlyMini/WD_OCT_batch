# constructor
# class method/ only
# cannot invoke the method
# __init__ is the method name
# this method invoked at teh time of object creation

# class myclass:
#
#     def __init__(self):
#         print("printing constructor")
#
# obj=myclass() # __init__ or constructor getting executed at the time of object creation
# #obj.__init__()


# class myclass:
#
#     def __init__(self,a,b):
#         c,d=30,40 ## c and d is instance variable
#         print(f"printing constructor {a} {b} {c} {d}") # a and b is instance variable
#
# obj=myclass(10,20) # instance variable created at the time of onject creation


# class myclass:
#
#     def __init__(self):
#         print("printing constructor1")
#
#     def __init__(self):
#         print("printing constructor2")
#
#     def __init__(self):
#         print("printing constructor3")
#
# obj=myclass() # if multiple constructor given ...last created const will get invoked


########################################################3

class myclass:

    def __init__(self,a,b):
        c,d=1,2
        var1=100
        var2=100
        self.var1=a
        self.var2=b
        self.var3=c
        self.var4=d

        self.a=var1
        self.b=var2

        myclass.var1=a
        myclass.var2=b
        myclass.var3=c
        # myclass.var4=d
        print(myclass) # holding the class name
        print(self) # holding the object
        print(f"printing constructor {a} {b} {c} {d}")

    def instance_method(self):
        print(self)
        # print(f"printing constructor {a} {b} {c} {d}")
        # print(f"printing inside instance method {self.a} {self.b} {self.c} {self.d}")
        # print(f"printing inside instance method {myclass.a} {myclass.b} {myclass.c} {myclass.d}")
        print(f"printing instance method {self.var1} {self.var2} {self.var3} {self.var4} {self.a} {self.b}")
        #print(f"printing instance method {myclass.var1} {myclass.var2} {myclass.var3} {myclass.var4}")
        #AttributeError: type object 'myclass' has no attribute 'var1'

    @classmethod
    def class_method(cls):
        print(cls)
        print(f"printing instance method {cls.var1} {cls.var2} {cls.var3} {cls.var4}")

    @staticmethod
    def static_method():
        print(f"printing instance method {var1} {var2} {var3} {var4}")

obj=myclass(10,20)
obj.instance_method()
obj.class_method()
#obj.static_method()
