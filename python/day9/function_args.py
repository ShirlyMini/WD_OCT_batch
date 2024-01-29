# args and kwargs

# args

# def myfunc(a,b,c,d):
#     print("hello")
#     print(a,b,c,d)
#
# #myfunc(10,20,30,40, 40) # TypeError: myfunc() takes 4 positional arguments but 5 were given

# def myfunc(*args):
#     print("hello")
#     print(args) # tuple
#     #print(args[2]) # tuple
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
#
#
# print(myfunc(10,2,3,4,5,6,7,8,90))

# kwags
# def myfunc(**kwargs):
#     print("hello")
#     print(kwargs) # dict
#     print(kwargs["a"]) # dict
#     sum=0
#     for i in kwargs.values():
#         sum=sum+i
#     return sum
#
# print(myfunc(a=20, b=3,c=4, d=50, e=30))


# nested func

# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return "hello", c + d
#     return inner_fun(a, b)
#
# print(outer_fun(5,10))

# def outer_func():
#     msg1="python"
#     def inner_func():
#         msg2="hello"
#         return msg1+msg2
#
#     #print(inner_func())
#     #(or)
#     return inner_func # ref of the func
#     #return inner_func()
#
# print(outer_func())
# var=outer_func()
# print(var)
# print(var())


# def myfunc():
#     msg1="python"
#     return msg1
#
# print(myfunc())
# print(myfunc)
# var_ref=myfunc
# print(var_ref)
# print(var_ref())


