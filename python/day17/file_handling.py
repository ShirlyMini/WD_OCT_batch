#######################
# write, read, overwriting
#open(path, mode)

# write data
# if no file exsit it will craete a file
# oif file exist it will overwrite the content in file
# fh=open("text1.txt", "w")#create
# fh.write("statement4\n")
# fh.write("statement5\n")
# fh.write("statement6\n")
# fh.close()

# append data
# if no file exsit it will craete a file and write the data
# if file exsit it will append the content in file

# fh=open("text2.txt", "a")#create
# fh.write("statement1\n")
# fh.write("statement2\n")
# fh.write("statement3\n")
# fh.close()

# read data

# reading the data # default mode
# no file exsiste#FileNotFoundError
# fh=open("text2.txt" ,"r")
# #fh=open("text2.txt")
# # print(fh.read())
# # print(type(fh.read()))# content to string
#
# print(fh.readlines())
# print(type(fh.readlines())) # content to list
#
# print(fh.readline())
# print(fh.readline())
# print(fh.readline())
# print(fh.readline())
# fh.close()


########################3

# with statement
# fh=open("text1.txt", "w")
# with open("text3.txt", "w") as fh:
#     fh.write("writing statement 1\n")
#     fh.write("writing statement 2\n")
#     fh.write("writing statement 3\n")
#
# with open("text3.txt") as fh:
#     print(fh.read())


################################
with open("text3.txt", "w") as fh:
    fh.write("writing statement 1\n")
    fh.write("writing statement 2\n")
    fh.write("writing statement 3\n")

with open("text3.txt") as fh:
    lines = fh.readlines()

with open("text3.txt","w") as fw:
    print(lines)
    for line in lines:
        #print(line[::-1])
        line1=line.strip("\n")
        print(line1)
        fw.write(line1[::-1])

