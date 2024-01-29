# list
# collection of datatypes  which is ordered and mutable
# square bracket
# changeable

# create list
# array=homogenous datatype
# list=heterogenous datatypes

# mylist=[10,20,30,40,50]
# print(mylist)#[10, 20, 30, 40, 50]
# mylist=["apple", "orange", "cherry"]
# print(mylist)#['apple', 'orange', 'cherry']
# mylist=[10,20, 30, 40, 50, "apple", "orange", "cherry"]
# print(mylist)#[10, 20, 30, 40, 50, 'apple', 'orange', 'cherry']
# mylist=list(["apple", "orange", "cherry"])
# print(mylist)#['apple', 'orange', 'cherry']
#
# # empty list
# mylist = list()
# print(mylist)
# mylist = []
# print(mylist)

# accessing element

# mylist=["apple", "orange", "cherry", "banana"]
# print(mylist[0])#apple
# print(mylist[-2])#cherry
# # print(mylist[4]) # index error for non exisiting index
# print(mylist[3:4])#['banana']
# print(mylist[::-1])#['banana', 'cherry', 'orange', 'apple']

#change element
# mylist=["apple", "orange", "cherry", "banana"]
# mylist[1] = "grape"
# print(mylist)

# for loop = reads all the element n the list
# mylist=["apple", "orange", "cherry", "banana"]
# #
# # for i in mylist:
# #     print(i)
#
# for i in mylist[1:3]:
#     print(i)
#
# for i in mylist[::-1]:
#     print(i)

# check the exsistence of element

# mylist=["apple", "orange", "cherry", "banana"]
# print("banana" in mylist)
# print("bananadcec" in mylist)
#
# length of list
#
# print(len(mylist[0]))
# print(len(mylist))

# add element
# mylist=["apple", "orange", "cherry", "banana"]
#
# # using append
# mylist.append("kiwi")
# print(mylist)
#
# # using insert
# mylist.insert(2,"Dragon frt")
# print(mylist)

# remove element
mylist=["apple", "orange", "cherry", "banana"]
#using pop
# mylist.pop() # element present at the last will get removed
# print(mylist)
# mylist.pop(1) # element present at the index will get removed
# print(mylist)

#using del

# del mylist[2]
# print(mylist)
# del mylist # deletes variable
# #print(mylist) # nameerror
#
# # using clear
# mylist.clear()
# #mylist.clear(1) #TypeError: list.clear() takes no arguments (1 given)
# print(mylist) # return empty list


# copy list

# mylist1=["apple", "orange", "cherry", "banana"]
# print(f"id mylist1 {id(mylist1)}")#id mylist1 1508372804544
#
# mylist2 = mylist1
# print(f"id mylist2 {id(mylist2)}")#id mylist1 1508372804544
# print(mylist2) # swallow copy #['apple', 'orange', 'cherry', 'banana']

# mylist2.remove("apple")
# print(mylist1)#['orange', 'cherry', 'banana']
# print(mylist2)#['orange', 'cherry', 'banana']



# print(f"id mylist2 {id(mylist2)}")#id mylist2 2967734547392
# mylist3 = list(mylist1) ## deep copy
# print(mylist3)
# print(f"id mylist3 {id(mylist3)}")
#
# mylist2.remove("apple")
# print(mylist1)#['orange', 'cherry', 'banana']
# print(mylist3)#['apple', 'orange', 'cherry', 'banana']


# mylist4 = mylist1.copy() # deep copy
# print(mylist4)#['apple', 'orange', 'cherry', 'banana']
# print(f"id mylist4 {id(mylist4)}")#id mylist4 2196163818048
# mylist4.remove("apple")
# print(mylist1)#['apple', 'orange', 'cherry', 'banana']
# print(mylist4)#['orange', 'cherry', 'banana']


# combine list
# list1=[10,20, 30, 40, 50]
# list2=["apple", "orange", "cherry"]
#
# # comparator operator
#
# # print(list1!=list2)
#
# # appr 1
# print(list1+list2)[10, 20, 30, 40, 50, 'apple', 'orange', 'cherry']
#
# # appr2
#
# for i in list2:
#     list1.append(i)
# print(list1) #[10, 20, 30, 40, 50, 'apple', 'orange', 'cherry']
#
# for i in list1:
#     list2.append(i)
# print(list2)#['apple', 'orange', 'cherry', 10, 20, 30, 40, 50]
#
# # appr3
#
# list1.extend(list2)
# print(list1)#[10, 20, 30, 40, 50, 'apple', 'orange', 'cherry']

# convert string to list
# str1="apple,orange,grape"
# list1=str1.split(",") # list
# print(list1)#['apple', 'orange', 'grape']
#
# str1="welcome to python"
# print(str1.split()) # splitting based on space#['welcome', 'to', 'python']
# print(str1.split("to")) # splittting based on "to"#['welcome ', ' python']

# convert list to string
# list1=['apple', 'orange', 'grape']
# print("".join(list1))
# print(",".join(list1))
# print(" and ".join(list1))