# array of bytes
# immutable
# str1="100shir;msxlknx"

# # ways to create strings
#
# str1='welcome'
# str1="welcome"
# str1=str('welcome')
# str1=str("welcome")
# print(str1)
# # # empty string
# n = ''
# n = ""
# n = str()
# print(n)

# mutable  and immutable
# are strings immutable? - yes

# str1="string"
# print(str1[3]) # index strats with 0 ends with n-1
# #str1[3] = "o" # TypeError: 'str' object does not support item assignment

# # id() - return location
# str1="welcome"
# print(id(str1)) # 1219678521904
#
# print(id(str1+"to python")) # 1219680177648
# str1 = str1 + "to python"
# print(id(str1)) # 1219680177648

# if the id value is changed after updation then it is called immutable

# Slicing
# n..-3 -2 -1 0 1 2 3 4 5 ..n
# str1="Welcome"
# # 0 to n-1
# # Reverse indexing-
# print(str1[0:3])
# print(str1[3:7])
# print(str1[1:-1])
# print(str1[0:7:3])
# print(str1[::]) # Welcome
# print(str1[::-1]) # emocleW
# print(str1[-1])
# print(str1[-2])
# print(str1[-3])

# a = 97

str1="b"
#print(int(str1)) # ValueError: invalid literal for int() with base 10: 'b'

print(ord(str1)) # char to  ascii value
#print(ord("str"))# TypeError: ord() expected a character, but string of length 3 found
print(chr(98)) # ascii value to char
print(str(98)) # "98"

