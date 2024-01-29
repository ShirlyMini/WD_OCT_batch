# collection of functions and class
# module1.py (funcn or class) how to access it from client file/another file

# # appr1
#
# import module1
#
# module1.add(2,3)
# module1.multiply(4,5)
#
# # app2
# # from module1 import add
# # from module1 import multiply
# from module1 import add, multiply
# add(2,3)
# multiply(4,5)
#
# # appro3
#
# from module1 import *
# add(2,3)
# multiply(4,5)


########################################################3
# modules with same func name

#appr1
# import module1,module2
#
# module1.add(1,2)
# module2.add(2,3)
# module1.multiply(5,6)
# module2.multiply(5,6)

# app2

# from module1 import add,multiply
# from module2 import add,multiply
#
# add(1,2)
# multiply(3,4)

# app3
# from module1 import *
# from module2 import *
#
# add(1,2)
# multiply(3,4)

##############################################33
# with classes
# appr1
# import module1
# import module2
# obj = module1.bird(1,2)
# obj.display()# inst meth
# module1.bird.show1()# class
# module1.bird.show2()# static
# print(module1.bird.var1)
# obj1=module2.animal()
# obj1.display()

# app2
# from module1 import bird
# from module2 import animal
#
# obj=bird(1,2)
# obj2=animal()
# obj.display()
# print(obj.var1)
# bird.show1()
# bird.show2()
# obj2.display()

# appr3

from module1 import *
# from module2 import *
#
# obj=bird(1,2)
# obj2=animal()
# obj.display()
# print(obj.var1)
# bird.show1()
# bird.show2()
# obj2.display()

obj3=A()
obj3.display()#this is class A module 2
print(f"from python_modules __name__:{__name__}")