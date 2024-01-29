# decorators


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


#
# def outer_func(func):
#     msg1="welcome"
#     def inner_func():
#         msg2=" to "
#         var=func()
#         return msg1+msg2+var
#     return inner_func()
#
# def printer1():
#     return "python"
#
# def printer2():
#     return "java"
# def printer3():
#     return "ruby"
#
# print(outer_func(printer1))
# print(outer_func(printer2))
# print(outer_func(printer3))


# def display_info(func_ref):
#     def inner():
#         print("executing fcntion::", func_ref.__name__)
#         func_ref()
#         print("finished")
#
#     return inner
#
# def mufunc1():
#     print("Hello World")

# var=display_info(mufunc1)
# var()
#  or
#  @display_info

# @display_info  # ---->decorator
# def myfunc2():
#     print("Hello python")
#
# myfunc2()
#
# @display_info  # ---->decorator
# def myfunc3():
#     print("Hello java")
#
# myfunc3()

# def outer_func(func):
#     msg1="welcome"
#     def inner_func():
#         msg2=" to "
#         var=func()
#         return msg1+msg2+var
#     return inner_func # return inner func reference
#
# @outer_func
# def printer1():
#     return "python"
# @outer_func
# def printer2():
#     return "java"
# @outer_func
# def printer3():
#     return "ruby"
#
# # print(outer_func(printer1))
# # print(outer_func(printer2))
# # print(outer_func(printer3))
#
# print(printer1())
# print(printer2())
# print(printer3())


# frozenset - unordered and immutable
# set - unordered and mutable

# fs=frozenset()
# print(fs)
#
# s=set()
# print(s)

# create
# myfs={1,2,3,4,5}
# print(myfs)
# print(type(myfs))
#
# myfs=frozenset({1,2,3,4,5})
# myfs=frozenset({"a", "b", "c", 1,2,3,4,5})
# print(myfs)
# print(type(myfs))

# myfs=frozenset({"a", "b", "c", 1,2,3,4,5})
# mys=set({"a", "b", "c", 1,2,3,4,5})
#
# #print(list(myfs))
#
# #myfs.add() #AttributeError: 'frozenset' object has no attribute 'add'
# myfs1=frozenset({"a", "b", "c", 1,2,3,4,5})
# print(myfs1, f"id:{id(myfs1)}")
# myfs2=myfs1 # swallow copy
# print(myfs2, f"id:{id(myfs2)}")
# myfs3=frozenset(myfs1) #  # swallow copy
# print(myfs3, f"id:{id(myfs3)}")
# myfs4=myfs1.copy() # swallow copy
# print(myfs4, f"id:{id(myfs4)}")