# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print(a) # galti -> 
# print("hello")
# print("hello")
# print("hello")
# print("hello")

#zero division error
# print(10/0)

#value error
# print(int("hello"))


# Type error
# print(5 + "A")


# IndexError
# a = [1,2,3,4]
# print(a[100])

# name error
# print(a)

# Attribute error
# a = 10
# a.append(100)

# fileNotFoundError
# open("abc.txt")


# import fsadf

# if x > 5

# print("start")
# try:
#     print(a)
# except:
#     print("exception handled")


# print("Rest of the 50 services")


# try:
#     a = int(input("enter your number: \n")) # valueError
#     print(10/a) # 10/0 -> ZeroDivisionError

# except ValueError:
#     print("a ki value nhi di hai")

# except ZeroDivisionError:
#     print("Zero ko Division nhi kr sakthe")

# else:
#     print("All Okay no Error")

# finally:
#     print("ALWAYS EXECUTED")

# else -> run only when try is okay

# raise - customize error

age = int(input("Enter age: "))
if age < 18:
    raise ValueError("Age m 18 se km hogi toh mt hi aana !!!!")


