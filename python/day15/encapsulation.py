# data hiding
# public member, private member, protected
###########################public###############
# class parent:
#     a="parent var"
#     def func_public(self):
#         print(self.a)
#         print("function public")
#
# obj=parent()
# obj.func_public()
###############################private#####################
# class parent:
#     __a="parent var"
#     def __func_private(self):
#         print("private var __a",self.__a)
#         print("function private")
#
#     def func_public(self):
#         print("private var __a",self.__a)
#         self.__func_private()
#         print("function public")
#
# class child(parent):
#     def child_func(self):
#         print("private var __a",self.__a)
#         self.__func_private()
#         print("function public")
#
# # obj=parent()
# # obj.func_public()
#
# obj=child()
# obj.child_func()# AttributeError: 'child' object has no attribute '_child__a'

##########################3protected#######################

# pseudo protected
class parent:
    _a="parent var"
    def _func_protected(self):
        print(self._a)
        print("function protected")

    def func_public(self):
        print(self._a)
        self._func_protected()

class child(parent):
    def func_public1(self):
        print(self._a)
        self._func_protected()

# obj=parent()
# obj._func_protected()
# obj.func_public()

obj=child()
obj.func_public1()
print(obj._a)