# class Parent1:
#
#     def __init__(self):
#         a="Instance varible in parenet1 class"
#         Parent1.a=a
#         print("Parent1 contructor")
#     def A(self):
#         print("Prining A method in ths Parent1 class")
# class Parent2:
#     def __init__(self):
#
#         a="Instance varible in parenet2 class"
#         Parent2.a=a
#         print("Parent2 contructor")
#     def A(self):
#         print("Prining A method in ths Parent2 class")
# class child(Parent1,Parent2):
#     def __init__(self):
#         a = "Instance varible in child class"
#         child.a=a
#         print("child contructor")
#
#     def A(self):
#         print("Prining A method in ths child class")
#         print(child.a)
#         super().A()
#         # print(Parent2.a)#AttributeError: type object 'Parent2' has no attribute 'a'. Did you mean: 'A'?
#         # print(Parent1.a)
#
#         Parent2.__init__(self)
#         Parent1.__init__(self)
#         print(Parent2.a)  # AttributeError: type object 'Parent2' has no attribute 'a'. Did you mean: 'A'?
#         print(Parent1.a)
#         Parent1()
#         Parent2()
#
# obj=child()
# obj.A()

#################################################3
class parent1:
    #a = "parent2 class variable"
    @classmethod
    def func1(cls, a):
        a = "parent1 variable_class"
        print("class method parent1")

    @staticmethod
    def func2(a):
        print("static method parent1")


class parent2:
    #a="parent2 class variable"
    @classmethod
    def func1(cls, a):
        a = "parent1 variable_class"
        print("class method parent2")

    @staticmethod
    def func2(a):
        a = "parent2 variable_static"
        print("static method parent2")


class child(parent2, parent1):
    a = "child variable"

    def myfunc(self):
        print("instance method child")

        parent1.func1(10)
        parent1.func2(20)
        parent2.func1(30)
        parent2.func1(40)
        print(self.a)
        print(parent1.a)
        print(parent2.a)


obj = child()
print("****************obj.func2****************")
obj.func2(10)#parent2
print("****************child.func2****************")
child.func2(10)#parent2
print("****************obj.func1****************")
obj.func1(10)
print("****************child.func1****************")
child.func1(30)
print("****************child.myfunc****************")
obj.myfunc()