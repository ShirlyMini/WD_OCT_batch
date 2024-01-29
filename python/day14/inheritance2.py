# single inheritance
#
# class parent1:
#     def func_parent1(self):
#         print("this is func_parent1")
#
#     def A(self):
#         print("this is parent1 func A")
#
# class child1(parent1):
#     def func_child1(self):
#         print("this is func_child1")
#         self.func_parent1()
#         super().func_parent1()
#         #print(super())  # used to access base class attributes#<super: <class 'child1'>, <child1 object>>
#         super().A()
#
#     def A(self):
#         print("this is child1 func A")
#         self.func_parent1()
#         super().func_parent1()
#         #print(super())# used to access base class attributes
#         super().A()
#
# obj=child1()
# obj.func_child1()
# # obj.func_parent1()
# obj.A()
# # obj1=parent1()
# # obj1.A()
#####################################################################3

# parent--> child1
# parent---> child2-->child3
# class Parent:
#     def fun_1(self):
#         print(self)
#         print("Parent class")
#
# class child1(Parent):
#     def fun_2(self):
#         print("Child 1 class")
# class child2(Parent):
#     def fun_3(self):
#         print("child 2 class")
# class child3(child2):
#     def fun_4(self):
#         print("child 3 class")
#
# obj = child3
# # print(child3)# class name
# # print(child3())# obj
# obj.fun_1("a")
#
#
# # obj1=child3()
# # obj1.fun_4()
# # obj1.fun_3()

#####################################################################3


class parent1:
    a="parent1 class var"
    def func_parent1(self):
        print("this is func_parent1")

    def A(self):
        print("this is parent1 func A")

class parent2:
    a="parent2 class var"
    def func_parent2(self):
        print("this is func_parent2")

    def A(self):
        print("this is parent2 func A")

class child1(parent1, parent2):
    a = "child class var"
    def func_child1(self):
        print("this is func_child1")
        print("parent1 attributes#####################3")
        self.func_parent1()
        super().func_parent1()
        #parent1.func_parent1()TypeError: parent1.func_parent1() missing 1 required positional argument: 'self'
        #print(super())  # used to access base class attributes#<super: <class 'child1'>, <child1 object>>
        super().A()
        parent1().A()
        # parent1.A()#TypeError: parent1.A() missing 1 required positional argument: 'self'
        print("parent2 attributes#####################3")
        self.func_parent2()
        super().func_parent2()
        super().A()
        parent2().A()
        print("Class variables#####################")
        print(self.a)
        print(super().a)
        print(parent1.a)
        print(parent2.a)

    def A(self):
        print("this is child1 func A")
        self.func_parent1()
        super().func_parent1()
        #print(super())# used to access base class attributes
        super().A()
        print("Class variables#####################")
        print(self.a)
        print(super().a)
        print(parent1.a)


obj=child1()
#obj.func_child1()
print(obj.a)
print(obj.A())
# obj.func_parent1()
#obj.A()
# obj1=parent1()
# obj1.A()


# method resolution order - child, parent class in the order the child inherited
# super() - if multiple parent, super will take first parent given in the child class
###########################################################3

