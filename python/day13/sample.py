# a="global variable"
# class myclass:
#     a="class variable"
#     def __init__(self):
#         print("______________Inside the constructor__________________")
#         a="constructor variable"
#
#         print(f"constructor variable {a}")
#         print(f"class variable{myclass.a}")
#         print(f"global variable{globals()['a']}")
#         #self.a = a
#         myclass.a = a
#
#     def inistancemethod(self):
#         print(f"constructor variable {self.a}")
#         print(f"class variable {myclass.a}")
#         print(f"global variable {a}")
#
#
#     @staticmethod
#     def staticmethod():
#         print(obj)
#         print(myclass)
#         print(f"constructor variable {a}")
#         print(f"class variable {myclass.a}")
#         print(f"global variable {a}")
#         print(f"global variable {globals()['a']}")
#
#     @classmethod
#     def classmethod(cls):
#         print(obj)
#         print(cls)
#         print(myclass)
#         print(f"constructor variable {cls.a}")
#         print(f"constructor variable {obj.a}")
#         print(f"class variable {myclass.a}")
#         print(f"global variable {a}")
#
# print("_______________Inside the class method-myclass name______________________")
# myclass.classmethod()
# obj = myclass()
# print("________________Inside instance method______________________")
#
# obj.inistancemethod()
# print("_______________Inside the static method_____________________")
#
# obj.staticmethod()
# print("_______________Inside the class method______________________")
#
# obj.classmethod()

# #
# class myclass:
#     def __init__(self,a):
#         print("constructor1")
#
#     def __init__(self,a,b):
#         print("constructor2")
#
#     def __init__(self, a, b,c):
#         print("constructor3")
#
#     # def __init__(self, a):
#     #     print("constructor4")
#
#     def instance1(self,a):
#         print("instance 1")
#     def instance1(self,a,b):
#         print("instance 2")
#
# # override is NA in python
# obj=myclass(10,20,30)
# obj.instance1(10,20)

#overload
# class myclass:
#     def __init__(self,*a): #overloading
#         print("constructor1")
#
# obj=myclass(10,20,30,40,50)

# a=10
# print(a)
# del a
# print(a)


# class myclass:
#     def __init__(self,a):
#
#         print(a)
#         self.a=a
#         print("constructor1")
#
#     def myfunc(self):
#         print("instance func")
#
#     def __del__(self):
#         print("destructor")
#
# obj=myclass(10)# instantiation
# obj.myfunc()
# print(obj.a)
# print(obj)
# obj.__del__()
# print(obj.a)
# obj.myfunc()
# print(obj)