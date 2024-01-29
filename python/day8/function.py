# set of statement that will be called to do specific task

# def keyword
# declaring the function
# invoke function

# ex1
# def myfunc(): # create
#     print("hello myfunc!!")
#
# # invoke
# myfunc()
# no para and no return

# def myfunc():
#     print(10+20)
#
# myfunc()#30

# para and return

# def addition(a, b):
#     return a+b
#
# var = addition(10,20)
# print(var)#30
# # or
# print(addition(30,40))#70

# with para and no return

# def myfunc(a):
#     print(f"Hello {a}")
#
# myfunc("John")#Hello John

# no para and with return

# def myfunc():
#     #return "Hello python!!"
#     #return 11
#     return [(((10,20,30)))]
# print(type(myfunc()))

# global and local variable
# global_var="this is global var"

# def myfunc():
#     local_var = "this is local var"
#     print(global_var, local_var)
#
#
# myfunc()#this is global var this is local var
# print(global_var,
#       local_var) #NameError: name 'local_var' is not defined.

# example 2 with same variable name

# x=10
#
# def myfunc():
#
#     print("inside function before initiating var x", x)
#
# print("before calling the function", x)#before calling the function 10
# myfunc()#inside function before initiating var x 10
# print("after calling the function", x)#after calling the function 10

# example 3


# x=10
#
# def myfunc():
#
#     print("inside function before initiating var x", x) # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
#     x=20
#     print("inside function after initiating var x", x)
#
# print("before calling the function", x)
# myfunc()
# print("after calling the function", x)

# example 4

# x=10
#
# def myfunc():
#     global x
#     print("inside function before initiating var x", x)
#     x=20
#     print("inside function after initiating var x", x)
#
# print("before calling the function", x)#before calling the function 10
# myfunc()#inside function before initiating var x 10
# #inside function after initiating var x 20
# print("after calling the function", x)#after calling the function 20


# ex 5
# a=1
#
# def func():
#     #print(a)
#     a=2
#     print("inside finc()", a)
#
# print("outside func() , before calling", a)#outside func() , before calling 1
# func()#inside finc() 2
# print("outside func() , after calling", a)#outside func() , after calling 1

#ex 6

# a=1
#
# def func():
#     print("inside func()", a)
#
# print("outside func() , before calling", a)#outside func() , before calling 1
# func()#inside func() 1
# print("outside func() , after calling", a)#outside func() , after calling 1

#ex 7
# a=1
#
# def func():
#     global a
#     a=3
#     print("inside func()", a)
#
# print("outside func() , before calling", a)#outside func() , before calling 1
# func()#inside func() 3
# print("outside func() , after calling", a)#outside func() , after calling 3


# 2 types of parametes
# positional para
# keyword para

# def addition(a,b,c,d):
#     return f"a:{a}+b:{b}+c:{c}+d:{d}={a+b+c+d}"

#print(addition())# TypeError: addition() missing 4 required positional arguments: 'a', 'b', 'c', and 'd'
#print(addition(10,20,30,40)) # postional
#print(addition(10,20,30)) #TypeError: addition() missing 1 required positional argument: 'd'
#print(addition(10,20)) #TypeError: addition() missing 2 required positional argument: 'c'and 'd'
#print(addition(a=10,b=20,c=30,d=40)) # keyword para
#print(addition(b=20,a=10,d=40, c=30)) # keyword para
#print(addition(a=10, 20,30,40)) #SyntaxError: positional argument follows keyword argument
#print(addition(20,30,40, a=10)) # TypeError: addition() got multiple values for argument 'a'
# print(addition(20,30,40, d=10))
# print(addition(20,30,c=40, d=10))
# print(addition(20,30,d=10, c=40))

# with default parameter
# def addition(a,b,c=10,d=20):
#     return f"a:{a}+b:{b}+c:{c}+d:{d}={a+b+c+d}"
#
# print(addition(10,20,30,40))
# print(addition(10,20))
# #print(addition(10))# TypeError: addition() missing 1 required positional argument: 'b'
# print(addition(a=10,b=20,c=30,d=40))
# print(addition(a=10,b=20))
# print(addition(a=10))# TypeError: addition() missing 1 required positional argument: 'b'
