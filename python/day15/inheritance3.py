# class parent1:
#     def __init__(self):
#         print("constructor from parent1")
#
#     def func1(self):
#         print("func1")
#
# class parent2:
#     def __init__(self):
#         print("constructor from parent2")
#
#     def func2(self):
#         print("func2")
#
# class child(parent1,parent2):
#     def __init__(self):
#         print("constructor from child")
#         super().__init__()# parent1
#         parent1()
#         parent2()
#         parent1.__init__(self)# staticmethod
#         parent2.__init__(self)# staticmethod
#
#     def func3(self):
#         print("func3")
#
# child()

######################################################################3
# class parent1:
#     def __init__(self):
#         a="parent1 instance var"
#         self.a = a
#         print("constructor from parent1")
#
#     def func1(self):
#         print("func1")
#
#
# class parent2:
#     def __init__(self):
#         a = "parent2 instance var"
#         self.a = a
#         print("constructor from parent2")
#
#     def func2(self):
#         print("func2")
#
#
# class child(parent1, parent2):
#     def __init__(self):
#         a = "child instance var"
#         self.a=a
#         print(self.a)
#         print("constructor from child")
#         super().__init__()  # parent1
#         print(self.a)
#         parent1.__init__(self)  # staticmethod
#         parent2.__init__(self)  # staticmethod
#         print(self.a)
#         ################current state will not get changed by using following#######
#         parent1().__init__()
#         print(self.a)
#         parent2().__init__()
#         print(self.a)
#         parent1()
#         parent2()
#         print(self.a)
#
#     def func3(self):
#         print("********************child func3****************")
#         print(self.a)
#         print("func3")
#
#
# obj=child()
# obj.func3()

# #################################################################
class parent1:
    def __init__(self):
        a="parent1 instance var"
        parent1.a = a
        print("constructor from parent1")

    def func1(self):
        print("func1")


class parent2:
    def __init__(self):
        a = "parent2 instance var"
        parent2.a = a
        print("constructor from parent2")

    def func2(self):
        print("func2")

class child(parent1, parent2):
    def __init__(self):
        a = "child instance var"
        child.a=a
        print(child.a)
        parent1.__init__(self)
        print(parent1.a)
        parent2.__init__(self)
        print(parent2.a)


    def func3(self):
        print("********************child func3****************")
        print(child.a)
        print(parent2.a)
        print(parent1.a)
        print("func3")


obj=child()
obj.func3()

#############################################################3

# class parent1:
#
#     @classmethod
#     def func1(cls,a):
#         print("class method parent1")
#
#     @staticmethod
#     def func2(a):
#         print("static method parent1")
#
# class parent2:
#
#     @classmethod
#     def func1(cls,a):
#         print("class method parent2")
#
#     @staticmethod
#     def func2(a):
#         print("static method parent2")
#
# class child(parent2,parent1):
#     def myfunc(self):
#         print("instance method child")
#         parent1.func1(10)
#         parent1.func2(20)
#         parent2.func1(30)
#         parent2.func1(40)



# obj=child()
# obj.func2(10)
# child.func2(10)
# obj.func1(10)
# child.func1(30)
# obj.myfunc()


# python pylo