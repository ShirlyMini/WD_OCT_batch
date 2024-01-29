# while
# for loop


#range()

#print 1 to 10

# range(n) = range(start=0, ends=n-1, step/increment=1)


# print(list(range(11))) # equal to range(0,11,1)
# print(list(range(0,11,2)))
# print(list(range(2,11,2)))

# while
# print 1 to 10
#initialize, condition, increment

# a=1 # init
#
# while a<=10: # cond
#     print(a)
#     #a=a+1 # incre
#     a+=1
#
# a=10 # init
#
# while a>=1: # cond
#     print(a)
#     #a=a-1 # decr
#     a-=1


#for loop = use along with range operator

# for var in range(1,11):# 0,1,2,..9
#     print(var)
#
# for var in range(10,0,-1):# 0,1,2,..9
#     print(var)

# jumping statement
# break
# continue
a=1
while a<=10: # cond
    print(a)
    #a=a+1 # incre
    if a==5:
        break
    a+=1


a=0
while a<=9: # cond

    #a=a+1 # incre
    a += 1
    if a==5:
        continue
    print(a)

