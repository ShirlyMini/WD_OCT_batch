##################################3
# 1)  raise
# 2) assert

# raise TypeError("error has been raised")
#
# raise Exception("error has been raised")
#
# raise AttributeError("error has been raised")

#Example 1

# n=-12
# if n>0 and n<110:
#     print("valid age")
# else:
#     raise AssertionError("invalid age")
#
# # assert( based on condition)#AssertionError
# n=-112
# assert n>0 and n<110#, ("invalid age")

# assert True
# assert False,(msg)

#########################################3
# with try except mech
# n=-12
# try:
#
#     if n>0 and n<110:
#         print("valid age")
#     else:
#         raise AssertionError("invalid age")
#
# #except Exception as msg:
# except AssertionError as msg:
#     print("exception happened", msg)
#
# else:
#     print("no error happened")
#
# finally:
#     print("finnaly block executed")


n=-12
try:
    assert n>0 and n<110, ("invalid age")

#except Exception as msg:
except AssertionError as msg:
    print("exception happened", msg)