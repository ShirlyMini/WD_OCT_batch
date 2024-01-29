# print("__name__ from file 1 outside condition", __name__)
# if __name__=="__main__":
#     import file2
#     print("__name__ from file 1", __name__)

# when the file exceuted as a script name==main
# when the file exceuted as modole name==module_name

def func1():
    print("this is func1")

if __name__=="__main__":
    func1()
