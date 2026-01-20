# def sum(a,b):
#     print(a+b)


# # function se apke code ki reusability badh jati hai
# # code efficiency store -> 

# sum(20,30)
# sum(3432,52435)

# 4 types -> normal, integer , string , boolean

#normal -> logic lekr aaye or wahi display ->
#function ke andr display hai --- call krthe samay display nhi krna hai
# function ke andr display nhi hai --- call krna hoga print()

def sum_1(a,b):
    sum = a+b
    print(sum)


def sum_2(a,b):
    return a+b


def check1(n):
    if(n >= 10):
        return "greater than 10"
    else:
        return "smaller than 10"
    

def check2(n):

    if n>=18:
        return True
    else:
        return False
    

def leapyear(n):
    # % 4 , 100 != 0 , 400 
    if n % 4 == 0 and (n%100 !=0 or n % 400 == 0):
        return "leap year hai"
    else:
        return "leap year nhi hai"
    

def demo(b,a=10):
    print(a+b)


def prime1(n):
    count = 0
    if n <=1:
        return False
    

    for i in range(2,n+1):
        if(n % i == 0):
            count+=1

    if(count == 1):
        return True
    else:
        return False
    

def prime2(n): #7
  
    if n <=1: 
        return False
    

    for i in range(2,n//2): #2,3
        if(n % i == 0):
           #7 % 3
           return False
    

    return True
    

