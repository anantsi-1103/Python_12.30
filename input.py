# a = float(input("Enter your Number: \n"))
# b = float(input("Enter your Number: \n"))
# print(a+b)
#  10 -> 10.5 , 10.5 - >10.5

# type casting -> type conversion -> 

# implicit -> apne aap hojate 
# explicit -> apko khud krna padtha hai

# 15 -> 15.0

# a = 10 # 10
# b = "20" # "20"
# d = int(b) # int("20") => 20
# c = a+d
# print(c)

a = 10
b = 2

# print(a+b)
# print(a-b)
# # single / -> float -> // -> to remain in int -> 2 
# print(a//b)
# print(a*b)
# print(a%b)

# print(a>b)  # true
# print(a>=b) # true
# print(a<b) # false
# print(a<=b) # false
# print(a==b) # false
# print(a!=b) # true

# print(a)


# # a = a + 100
# a = 100

# print(a)

# age = 4
# if(age >= 28):
#     print("Allowed")

# else:
#     print("Not Allowed")


# n = int(input("Enter your Number \n"))

# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# if else if -> 

# a = int(input("Enter your Number \n"))
# b = int(input("Enter your Number \n"))
# c = int(input("Enter your Number \n"))

# # greatest of 3 number
# if ((a>b)and(a>c)):
#     print(f"{a} : A is a greatest number of all")
# elif((b>a)and(b>c)):
#     print(f"{b} : B is a greatest number of all")
# else:
#     print(f"{c} : C is a greatest number of all")


# nested if -> 

# age = 29
# dl = "yes"

# if(age >= 18):
#     if(dl == "yes"):
#         print("Yes u r allowed")
#     else:
#         print("Yes allowed but apply for DL")
# else:
#     print("Below age")

# ternary operator -> 
# single line logic likhna hoga -> ternary operator 


# store 
# n = 10
# result = "Even" if n % 2 == 0 else "Odd"

# variable = 'true statement' condition else 'false statement'

a = int(input("Enter your Number \n"))
b = int(input("Enter your Number \n"))
c = int(input("Enter your Number \n"))


result = "A" if((a>b and a>c)) else "B" if((b>a) and (b>c)) else "C"

print(result)