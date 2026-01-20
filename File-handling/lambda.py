


# def sum(a,b):
#     return a+b


# add = lambda a,b : (a+b)

# print(add(10,20))
# print(sum(34,54))

# print(type(add))
# print(type(sum))

# lambda without variables
# print((lambda x : x*x)(5))

# map  -> use to apply a function to each element of an iterable
# , filter , reduce 

# n = [1,2,3,4]
# s = list(map(lambda x : x*x,n))
# print(s)
#[1,2,3,4]
#[1,4,9,16]


# filter -> filter the data based on the condition

# n = [1,2,3,4,5,6,7,8,9,10]
# even = list(filter(lambda x : x % 2 == 0,n))

# print(even)

#reduce -> reduce the sequence to a single value 

from functools import reduce 

n = [1,2,3,4,5,6,7,8,9,10]

sum = reduce(lambda a,b : a+b,n)

print(sum)