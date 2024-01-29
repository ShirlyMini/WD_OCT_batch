# set
# collection of datatypes  which is unordered and unindexed
# curly bracket{}
# changeable or mutable

# create

# set1={"apple", "orange", "cherry", "banana"}
# print(set1)#{'apple', 'orange', 'banana', 'cherry'}
#
# # empty set
# myset=set()
# print(myset)#set()
# print(type(myset))#<class 'set'>
# myset= {}
# print(myset)# dict
# print(type(myset)) # <class 'dict'>

# accessing element
#
# set1={"apple", "orange", "cherry", "banana"}
# #print(set1[0]) #TypeError: 'set' object is not subscriptable
# for i in set1:
#     print(i)

# indirect way
# list1=list(set1)
# print(list1)
# print(list1[-2])

# add/ update set

# set1={"apple", "orange", "cherry", "banana"}
#
# set1.add("kiwi") # single item
# print(set1)#{'kiwi', 'apple', 'orange', 'banana', 'cherry'}
#
# set1.update({"kiwi", "dragon frt"}) # multiple item
# print(set1)#{'kiwi', 'apple', 'orange', 'banana', 'cherry', 'dragon frt'}
#
# print(len(set1))#6

# remove item

# set1={"apple", "orange", "cherry", "banana"}
# set1.pop()
# print(set1)#{'apple', 'banana', 'orange'}
# set1.remove("orange")
# print(set1)#{'apple', 'banana'}
# set1.discard("cherry")
# print(set1)#{'apple', 'banana'}


# with non exsisting item
# set1.remove("kiwi") #KeyError: 'kiwi'
# print(set1)

# set1.discard("kiwi")
# print(set1) # no error
#
# set1.clear()
# print(set1) # empty set

# copy
set1={"apple", "orange", "cherry", "banana"}
# print(f"set1: {set1} id : {id(set1)}")#set1: {'orange', 'banana', 'apple', 'cherry'} id : 2265804951776
# set2=set1
# print(f"set2: {set2} id : {id(set2)}")#set2: {'orange', 'banana', 'apple', 'cherry'} id : 2265804951776
#
# set2.remove("apple")
# print(f"set1: {set1} id : {id(set1)}")#set1: {'banana', 'cherry', 'orange'} id : 1706357084384
# print(f"set2: {set2} id : {id(set2)}") # shallow copy
# #set2: {'banana', 'cherry', 'orange'} id : 1706357084384
#

# set3=set(set1) # deep copy
# print(f"set3: {set3} id : {id(set3)}")#set3: {'cherry', 'banana', 'apple', 'orange'} id : 2220038408672
# set3.remove("apple")
# print(f"set1: {set1} id : {id(set1)}")#set1: {'cherry', 'banana', 'apple', 'orange'} id : 2220038413600
# print(f"set3: {set3} id : {id(set3)}")#set3: {'cherry', 'banana', 'orange'} id : 2220038408672

# set4=set1.copy() # deep copy
# print(f"set4: {set4} id : {id(set4)}")#set4: {'banana', 'orange', 'apple', 'cherry'} id : 2205311158752
# set4.remove("apple")
# print(f"set1: {set1} id : {id(set1)}")#set1: {'banana', 'orange', 'apple', 'cherry'} id : 2205311163680
# print(f"set4: {set4} id : {id(set4)}")#set4: {'banana', 'orange', 'cherry'} id : 2205311158752

# join / comine
# set1={"apple", "orange", "cherry", "banana"}
# set2={10,20,30}
# set4={10,20,40}
#
# set3=set1.union(set2)
# print(set3)#{'cherry', 'orange', 'banana', 10, 20, 'apple', 30}
# # print(set2+set1) # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(set4.intersection(set2))#{10, 20}
#
#
# # with duplicate
s1={1,2,3,1,2,3}
print(s1)

s1=[1,2,3,1,2,3]
print(s1)

s1=(1,2,3,1,2,3)
print(s1)

rainbow = ('violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red')
# create a frozenset
f_set = frozenset(rainbow)

print(f_set)#{'green', 'yellow', 'indigo', 'red', 'blue', 'violet', 'orange'}