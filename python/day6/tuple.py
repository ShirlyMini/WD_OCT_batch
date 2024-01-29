# tuple
# collection of datatypes  which is ordered and immutable
# round bracket
# not changeable

# cannot modify the tuple
# append, insert, remove , new value in tuple
# copy

# mytuple=(10,20,30,40,50)
# print(mytuple)#(10, 20, 30, 40, 50)
# mytuple=("apple", "orange", "cherry")
# print(mytuple)#('apple', 'orange', 'cherry')
# mytuple=(10,20,30,40,50, "apple", "orange", "cherry")
# print(mytuple)#(10, 20, 30, 40, 50, 'apple', 'orange', 'cherry')
# mytuple=tuple((10,20,30,40,50, "apple", "orange", "cherry"))
# print(mytuple)#(10, 20, 30, 40, 50, 'apple', 'orange', 'cherry')
#
# # empty tuple
#
# mytuple = tuple()
# print(mytuple)
# mytuple = ()
# print(mytuple)

# accessing element
# mytuple=("apple", "orange", "cherry")
# print(mytuple[0])#apple
# print(mytuple[-1])#cherry
# print(mytuple[1:3])#('orange', 'cherry')
# print(mytuple[::-1])#('cherry', 'orange', 'apple')

# read all elements in tuple

# mytuple=("apple", "orange", "cherry", "kiwi")
# #
# for i in mytuple:
#     print(i)
# #
# for i in mytuple[::-1]:
#     print(i)

# change element
# mytuple=("apple", "orange", "cherry", "kiwi")
# mytuple[0] = "grape"
# print(mytuple) # TypeError: 'tuple' object does not support item assignment

# indirect way
# mylist = list(mytuple) # tuple  to list
# mylist[0]="grape"
# print(mylist)#['grape', 'orange', 'cherry', 'kiwi']
# mytuple=tuple(mylist) # list to tuple
# print(mytuple)#('grape', 'orange', 'cherry', 'kiwi')

# exsistence of elem
# mytuple=("apple", "orange", "cherry", "kiwi")
# print("apple" in mytuple)#True
# print("appledffv" in mytuple)#False
#
#
# #length of tuple
# print(len(mytuple))

# del function
# mytuple=("apple", "orange", "cherry", "kiwi")

#del mytuple[0] # TypeError: 'tuple' object doesn't support item deletion
# del mytuple
# print(mytuple)

# copy function

# mytuple1=("apple", "orange", "cherry", "kiwi")
# print(mytuple1)#('apple', 'orange', 'cherry', 'kiwi')
# print(f"id of mytuple1 {id(mytuple1)}")#id of mytuple1 2053749504528
# mytuple2=mytuple1
# print(mytuple2)#('apple', 'orange', 'cherry', 'kiwi')
# print(f"id of mytuple2 {id(mytuple2)}") #id of mytuple2 2053749504528# swallow copy coz ID is same
#
# mytuple3=tuple(mytuple1)
# print(mytuple3)
# print(f"id of mytuple3 {id(mytuple3)}") # swallow copy coz ID is same#id of mytuple3 1732781701648
#
# mytuple4=mytuple1.copy()
# print(mytuple4)
# print(f"id of mytuple4 {id(mytuple4)}") # AttributeError: 'tuple' object has no attribute 'copy'


# join / combine

tup1=(10,20,30)
tup2=("apple", "orange", "cherry", "kiwi")

print(tup1+tup2)#(10, 20, 30, 'apple', 'orange', 'cherry', 'kiwi')
print(tup1)
print(tup2)


# comparator operator

print(tup1==tup2)
