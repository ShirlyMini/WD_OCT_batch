# error or exception handling
# print("statement1")
# print("statement1")
# print("statement1")
# print(a)
# print("statement1")
# print("statement1")
# print("statement1")
# print("statement1")

#print(a)#NameError: name 'a' is not defined
# if 5>2#SyntaxError: expected ':'
#     print(True)

#print("10" + 10)#TypeError: can only concatenate str (not "int") to str

# to list all the error
# import builtins
# print(dir(builtins))


################################################33
# print("statement1")
# print("statement1")
# print("statement1")
# try:
#     #a=10
#     print(a)
# except:
#     print("error happened!!!")
# print("statement1")
# print("statement1")
# print("statement1")
# print("statement1")

# print("statement1")
# print("statement1")
# print("statement1")
# try:
#     print(1/0)
# except Exception as var:
#     print("error captured")
#     print(var)
# print("statement1")
# print("statement1")
# print("statement1")
# print("statement1")


# print("statement1")
# print("statement1")
# print("statement1")
# try:
#     #a=10
#     print(a)
#     #print("10" + 10)
#     #print(1/0)
#     # if 5>2
#     #     print(True)# syntax error will not get caugth in exception
#     # if 5>2:
#     # print(True)# IndentationError: expected an indented block after 'if' statement on line 65
# except ZeroDivisionError as var:
#     print("ZeroDivisionError handled")
#     print(var)
# except TypeError as var:
#     print("TypeError handled")
#     print(var)
# except NameError as var:
#     print("NameError handled")
#     print(var)
# except Exception as var:
#     print("error handled")
#     print(var)
# print("statement1")
# print("statement1")
# print("statement1")
# print("statement1")

############################################3
# else and final block
# print("statement1")
# print("statement1")
# print("statement1")
# print("statement1")
try:
    #a=10
    print(a)
except Exception as var:
    print("Exception block", var)
else:# exception not occured
    print("exception not happen proceeding further")
finally:
    print("final block proceeding further")
# print("statement1")
# print("statement1")
# print("statement1")
# print("statement1")

#################################################
# user induced error

# assert (error happen based on condtion)
# raise

#raise Exception("exception caught")
#raise ZeroDivisionError("msg")
#raise AssertionError("shirly")
# raise TypeError("msg")