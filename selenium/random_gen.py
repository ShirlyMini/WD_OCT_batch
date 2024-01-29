#"abc123@gmail.com"
# import string
# import random
#
# print(string.ascii_letters+string.digits)
# print(random.choice(string.ascii_letters+string.digits))
# email_gen=""
# for i in range(8):
#     email_gen = email_gen+random.choice(string.ascii_letters + string.digits)
# print(email_gen)
from os import popen


#############
# #############################3
# def addition(a,b):
#     return a+b
#
# print(addition(2,3))
#
# # anonymous function
# var = lambda a,b,c:a+b+c
# print(var(2,3, 4))

# import os
#
# var = os.popen("HELP", "r")
# print(var.read())

import subprocess

subprocess.run("help")
# subprocess.run("ssh root@<ip>")
# subprocess.run("password")
