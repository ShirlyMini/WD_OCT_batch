# control statements
# 1. conditional statement
# 2. looping statements
# 3. jumping statements

# Conditional statements
# 1. if...
# 2. if..else
# 3. if..elif..else

print("statement1")
print("statement2")
print("statement3")
print("statement4")
if False:
    print("statement5")
    print("statement5")
    print("statement5")
    print("statement5")
print("statement6")
print("statement7")
print("statement8")
print("statement9")
print("statement10")

# example 2
# n=2001
# print(n%4==0)
# if n%4==0:
#     print("leap year")

# example 3

n=2000
print(n%4==0)
if n%4==0:
    print("leap year")
else:
    print("Not Leap year")

# example4

age=12

if age>=18:
    print("eligible for Vote")
    print("hello")
else:
    print("not eligible for vote")
    print("hello")

# example5
#single line

#age=25
#print("eligible for Vote" if age>=18 else "not eligible for vote")
#{print("eligible for Vote"), print("hello")} if age>=18 else {print("not eligible for vote"), print("hello")}

# multiple condition
# if..elif..else

n=7

if n==1:
    print("Sunday")
elif n==2:
    print("Monday")
elif n==3:
    print("Tuesday")
elif n==4:
    print("wednesday")
elif n==5:
    print("thusday")
elif n==6:
    print("Friday")
elif n==7:
    print("Saturday")
else:
    print("invalid input")

# vote eligibility

age=18

if age>=18 and age>=1:
    print("eligible")
else:
    print("not eligible")





