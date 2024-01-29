# key and value pair which is unordered and indexed[key]
# written in curly brackets and they have key and value pair
# keys  values
# K1     v1
# K2     V2
# K3     V3
# K4     V1
# keys are unique but value can duplicate

# create

# mydict= {"brand":"Maruthi", "year": "2023", "model":1102}
# print(mydict)#{'brand': 'Maruthi', 'year': '2023', 'model': 1102}
# mydict= {101:"ram", 102:"sam", 103:"anne"}
# print(mydict)#{101: 'ram', 102: 'sam', 103: 'anne'}
# mydict=dict({"brand":"Maruthi", "year": "2023", "model":1102})
# print(mydict)#{'brand': 'Maruthi', 'year': '2023', 'model': 1102}
#
# with duplicate key
# mydict={"brand":"Maruthi", "year": "2023", "model":1102, "brand":"hyndai", "brand":"Maruthi123", }
# print(mydict)

# accessing values
# mydict= {"brand":"Maruthi", "year": "2023", "model":1102, "brand":"hyndai"}
# print(mydict)
# # ex1
# print(mydict["brand"])#hyndai
# print(mydict["year"])#2023
# print(mydict["model"])#1102
#
# #ex2
# print(mydict.get("brand"))#hyndai
# print(mydict.get("year"))#2023

# change values
# mydict= {"brand":"Maruthi", "year": "2023", "model":1102}
# print(mydict)#{'brand': 'Maruthi', 'year': '2023', 'model': 1102}
# mydict["year"] = "2020"
# print(mydict)#{'brand': 'Maruthi', 'year': '2020', 'model': 1102}
#
# # to change more than one key value
# mydict.update({"year": "2022"})
# print(mydict)#{'brand': 'Maruthi', 'year': '2022', 'model': 1102}
# mydict.update({"brand": "hero", "model": 1103})
# print(mydict)#{'brand': 'hero', 'year': '2022', 'model': 1103}

# read items using for loop

# mydict= {"brand":"Maruthi", "year": "2023", "model":1102}
# #appr 1
# for i in mydict:
#     print(i) # prints key
#
# for i in mydict:
#     print(mydict[i])# prints value

# appr 2

# print(mydict.keys())#dict_keys(['brand', 'year', 'model'])
# print(list(mydict.keys())[2])
# print(mydict.values())
# print(list(mydict.values())[1])#dict_values(['Maruthi', '2023', 1102])
#
# for key in mydict.keys():
#     print(key)
# #
# for val in mydict.values():
#     print(val)
# #
# mydict= {"brand":"Maruthi", "year": "2023", "model":1102}
# print(mydict.items())#dict_items([('brand', 'Maruthi'), ('year', '2023'), ('model', 1102)])
# print(list(mydict.items())[1][0])
# print(list(mydict.items())[1][1])
#
# for key, val in mydict.items():
#     # print(key, val)
#     if "brand" == key:
#         print(val)

# # check exesistence of key
# mydict= {"brand":"Maruthi", "year": "2023", "model":1102}
#
# print("model" in mydict.keys())# true
# print("20231wded" in mydict.values()) #false
# print(len(mydict))#3
# print(len(mydict.keys()))#3
# print(len(mydict.values()))#3

#
# mydict= {"brand":None, "year": "2023", "model":1102}
# mydict= {"brand":"", "year": "2023", "model":1102}
# print(mydict)

# mydict= {"":"muruti", "year": "2023", "model":1102}
# mydict= {None:"muruti", "year": "2023", "model":1102}
# print(mydict[None])

# add new key and val

# mydict= {"brand":"muruti", "year": "2023", "model":1102}
# # ex 1
# mydict["color"]="Black"
# print(mydict)#{'brand': 'muruti', 'year': '2023', 'model': 1102, 'color': 'Black'}
#
# # ex2
# mydict.update({'color': 'white', "seats": "6"})
# print(mydict)#{'brand': 'muruti', 'year': '2023', 'model': 1102, 'color': 'white', 'seats': '6'}
# print(list(mydict.keys())[0])

# remove dict item
mydict= {"brand":"muruti", "year": "2023", "model":1102}
# appr 1
print(mydict.pop("brand"))#muruti...(removes and return the value of the key removed)
print(mydict)#{'year': '2023', 'model': 1102}
#mydict.pop("brand")
#print(mydict)
# appr 2

# print(mydict.popitem())#('model', 1102)..removes the item randomly and returns the item in tuple
# print(mydict)#{'brand': 'muruti', 'year': '2023'}
#
# # clear
# mydict.clear()
# print(mydict)#{}

# del func
# mydict= {"brand":"muruti", "year": "2023", "model":1102}
# del mydict["brand"]
# print(mydict)#{'year': '2023', 'model': 1102}
# del mydict
# print(mydict)#NameError: name 'mydict' is not defined. Did you mean: 'dict'?

# copy
# mydict1= {"brand":"muruti", "year": "2023", "model":1102}

# print(f" mydict1:{mydict1} id : {id(mydict1)}")#mydict1:{'brand': 'muruti', 'year': '2023', 'model': 1102} id : 1615163519360
# mydict2=mydict1 # swallow copy
# mydict2.pop("brand")
# print(f" mydict1:{mydict1} id : {id(mydict1)}")#mydict1:{'year': '2023', 'model': 1102} id : 1543279702400
# print(f" mydict2:{mydict2} id : {id(mydict2)}")#mydict2:{'year': '2023', 'model': 1102} id : 1543279702400
#
# mydict3=mydict1.copy() # deep copy
#
# print(f" mydict1:{mydict1} id : {id(mydict1)}")#mydict1:{'brand': 'muruti', 'year': '2023', 'model': 1102} id : 2641343967616
# print(f" mydict3:{mydict3} id : {id(mydict3)}")#mydict3:{'brand': 'muruti', 'year': '2023', 'model': 1102} id : 2641343968256
#
# mydict4=dict(mydict1) # deep copy
# print(f" mydict1:{mydict1} id : {id(mydict1)}")#mydict1:{'brand': 'muruti', 'year': '2023', 'model': 1102} id : 2722310287744
# print(f" mydict4:{mydict4} id : {id(mydict4)}")#mydict4:{'brand': 'muruti', 'year': '2023', 'model': 1102} id : 2722310815104

# combine

mydict1= {"brand":"muruti", "year": "2023", "model":1102}
mydict2= {101:"ram", 102:"sam", 103:"anne"}

#print(mydict1+mydict2) # typeerror

mydict1.update(mydict2)
print(mydict1)#{'brand': 'muruti', 'year': '2023', 'model': 1102, 101: 'ram', 102: 'sam', 103: 'anne'}

# update - add, update, combine