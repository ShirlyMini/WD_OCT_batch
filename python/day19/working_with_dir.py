import os

# print(os.getcwd())#C:\Users\user\PycharmProjects\pythonProject_WDBatch\python\day19
# print(os.listdir())# current wworking dir/file
# print(os.listdir(r"C:\Users\user\PycharmProjects\pythonProject_WDBatch\python"))
# print(os.path.join(r"C:\Users\user\PycharmProjects\pythonProject_WDBatch", "python1"))
#print(os.mkdir(os.path.join(r"C:\Users\user\PycharmProjects\pythonProject_WDBatch", "python1")))
#print(os.mkdir(r"C:\Users\user\PycharmProjects\pythonProject_WDBatch\python2"))
#print(os.remove("text1"))
#print(os.rmdir("sample"))
#print(os.rmdir(r"C:\Users\user\PycharmProjects\pythonProject_WDBatch\python2"))
var=os.getcwd()
os.chdir(os.getcwd())
os.chdir("..")# previous dir
print(os.getcwd())
os.mkdir("python4")
print(os.listdir())
os.chdir(var)
print(os.getcwd())

