# pack1--> mod1, mod2--> func1, func2---> access it in client files
# import pack1---> cannot access modules or function inside the pcak1 package
# from pack1 import mod1, mod2
# #from pack1 import mod2
# mod1.display()
# mod2.show()

# from pack1.mod1 import display
# from pack1.mod2 import display, show
#
# display()
# show()

############################################

# import pack1.mod1
# pack1.mod2.add(2,3)
# pack1.mod1.add(2,3)

# from pack1 import mod2, mod1
#
# obj1=mod1.bird(1,2)
# obj1.display()
# print(obj1.var1)
# obj1.show1()
# obj1.show2()
# obj2=mod2.animal()
# obj2.display()

# from pack1.mod1 import bird, A
# from pack1.mod2 import animal, A
#
# obj1=bird(1,2)
# obj1.display()
# print(obj1.var1)
# obj1.show1()
# obj1.show2()
# obj2=animal()
# obj2.display()

# from pack1.pack2.mod3 import display
# display()
#
# from pack1.pack2 import mod3
# mod3.display()

# import pack1
# pack1.pack2.mod3.display()

# import pack3
# pack3.mod4.display()

import pack3.mod4
pack3.mod4.display()

# import pack1
# pack1.mod1.display()
import pack1.mod1
pack1.mod1.display()