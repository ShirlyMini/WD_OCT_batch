# parent class/base class/super class
#child class/derived class/subclass


# class personalloan:
#     def personal_loan(self):
#         print("personal loan")
#
# class homeloan:
#     def home_loan(self):
#         print("home loan")
#
# class vehicleloan:
#     def vehicle_loan(self):
#         print("vehicle loan")

# # class loan(personalloan): # sihgle inheritance
# #     def loan_func(self):
# #         print("child class")
# obj=loan()
# obj.loan_func()

# class loan(personalloan, homeloan, vehicleloan): # multiple inheritance
#     def loan_func(self):
#         print("child class")
#
# obj=loan()
# obj.loan_func()
# obj.personal_loan()
# obj.vehicle_loan()
# obj.home_loan()

# multilevel
# parent--> paremt1-> ..parentn-->child
class A:
    def func_a(self):
        print("function a")

class B(A):
    def func_b(self):
        print("function b")

class C(B):
    def func_c(self):
        print("function c")


obj=C()
obj.func_a()
obj.func_b()
obj.func_c()

#hirerchy
# one parent two child
class A:
    def func_a(self):
        print("function a")

class B(A):
    def func_b(self):
        print("function b")

class C(A):
    def func_c(self):
        print("function b")

obj_b=B()
obj_b.func_b()
obj_b.func_a()
obj_c=C()
obj_c.func_c()
obj_c.func_a()

# hybrid inheritance is combination of sigle, multiple, multilevl, hirerchy