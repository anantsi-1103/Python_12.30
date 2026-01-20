# def hello(n):
#     # base case 
#     if n == 0:
#         return
    
#     # kaam
#     print('hello')
#     return hello(n-1)


# hello(5)

# #sum , factorial , fibonacci 


def sum_n_natural(n): # 
    sum = 0 # 
    for i in range(1,n+1): # 1 2 3 4 5
        sum = sum + i 
        #

    return sum


def sum_recursion(n): # 5 4
    # 5------1
    # base case
    if n == 0:
     return n

    #kaam
    return n + sum_recursion(n-1)
# 4 + func(3)
def factorial(n): # 5 4
    # 5------1
    # base case
    if n == 1:
     return n

    #kaam
    return n * factorial(n-1)
# 4 + func(3)

def fibo(n):
   if(n==1 or n==0):
      return n
   
   return fibo(n-1) + fibo(n-2)

def count(si,ei):
   if(si >= ei):
      return si
   
   print(si)
   return count(si+1,ei)

print(count(1,100))
#1,
