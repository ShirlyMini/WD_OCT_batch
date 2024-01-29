# to reverse string using function
# print(list(reversed("Welcome")))
# print("".join(list(reversed("Welcome"))))
# str1="welcome"
# print(str1[::-1])

# function
# str1="abcde"
# print(max(str1))
# print(min(str1))
# print(len(str1)) # number of char

# using "in and "not in" operator
#
# s="welcome to python"
#
# print("python" in s) # true
# print("python" not in s) # False
# print("pythonxdsxerd" not in s) # True
# print("pythonxdsxerd" in s) # False

# string comparator

# print("tom" == "tome")
# print("tom" != "tome") # True
# print("tom" > "tome")
# print("tom" < "tome")

# test string

# str1="welcometopython"
# str2="python123"
# str3="123456"
# print(str1.isalnum()) # string contains num # T
# print(str2.isalnum()) # string contains num # T
# print(str3.isalnum()) # string contains num # T
# print(str1.isalpha()) # string contains alphabet #
# print(str2.isalpha()) # string contains alphabet #
# print(str3.isalpha()) # string contains alphabet #
# print(str1.isdigit()) # only number
# print(str2.isdigit()) # only number
# print(str3.isdigit()) # only number
#str4="123await"
# str4="welcome"

#The isidentifier() method returns True if the string is a valid identifier, otherwise False.

# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
# A valid identifier cannot start with a number, or contain any spaces.
# print(str4.isidentifier())

#'õ' 'ß' â # not ascii value

# print('ß'.isascii())
# print("12345".isascii())
# print("#@!$%".isascii())


# str1="welcometopython"
# str2="Welcometopython"
# str3="WELCOME"
# print(str1.islower())
# print(str2.islower())
# print(str1.isupper())
# print(str2.isupper())
# print(str3.isupper())

# str1="    "
# str2="     welcome"
# print(str1.isspace()) # only space
# print(str2.isspace())
# str1="Welcome To Python"
# print(str1.istitle())



# searching substring

# str1="Welcome To Python"
# print(str1.endswith("on"))
# print(str1.endswith("in"))
# print(str1.startswith("Wel"))
# print(str1.startswith("el"))
# print(str1.find("python")) # -1
# print(str1.index("python")) # ValueError: substring not found


# Testing strings


str1="welcome python"
str2="welcome"
str3="welcome123"
str4="123456"

str5="   "
str6="Welcome Python Is"
str7="WELCOME"
str8="123.456"
# print(str1.isalpha()) # false
# print(str2.isalpha()) # True
# print(str3.isalpha()) #false
# print(str4.isalpha()) #false

# print(str1.isalnum())
# print(str2.isalnum())
# print(str3.isalnum())
# print(str4.isalnum())
#
# print(str1.isspace())
# print(str2.isspace())
# print(str3.isspace())
# print(str4.isspace())
# print(str5.isspace())
#
# print(str1.istitle())
# print(str6.istitle())
#
# print(str2.isupper())
# print(str2.islower())
# print(str7.isupper())
# print(str7.islower())
#
print(str4.isdigit())
print(str3.isdigit())
# print(str3.isdecimal())
# print(str4.isdecimal())
# print(str8.isdigit())
# print(str8.isdecimal())
# print(str8.isnumeric())
# print(str4.isnumeric())
# print(str3.isnumeric())