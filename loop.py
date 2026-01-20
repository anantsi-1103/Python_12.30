# for , while , do while , nested loop 


# 1(intilization) ---- 1000(condition) ------- work-----  i+=1(updation)

# i = 1 #1 2 101
# while(i<=100): #T T
#     print(i) # 1 2 100
#     i = i + 1 # U U U


# n = int(input("Enter your Number : "))
#  # 1 - 10
# i = 1
# while(i<=20):
#     if(i==11):
#         break
#     # 7(n) x 1(i) = 7(n*i)
#     print(f'{n} x {i} = {n*i}')
#     i+=1

# 

# i = 1 #1 2 3
# while(i<=5): #T T T
#     if(i==3): #F F T
#         print("break")
#         break # terminate
#     print(i) # 1 2
#     i+=1 # U U

# continue - bypass 

# jump -> fall through -> 
# i = 1 # 3
# while(i<=5): 
#     if(i==3): # t
#         i+=1
#         print("continue")
#         continue
#     print(i)
#     i+=1

# i = 0 
# while(i<=100):

#     if(i == 0):
#         i+=2
#         print("continue")
#         continue
    
#     print(i)
#     i+=2

# for -> range() -> 

# for i in range(11):
#     print(i)

# sum of n natural number -> 


n = int(input("Enter your Number : ")) # 5
# i = 1 # 1 2 3 4 5 6
# sum = 0 # 0 1 3 6 10 15
# while(i<=n): # T T T T T F
#     sum = sum + i # 15
#     i+=1 # U U U U U

# print(sum)

# sum = 0
# for i in range(1 , n+1):    
#     sum += i

# print(sum)

# factorial -> 1*2*3*4*5

# i = 1
# fact = 1
# while(i<=n):
#     fact *= i
#     i+=1

# print(fact)

# prime number -> 

count = 0

if n == 1:
    print("not Prime")

for i in range(2, n+1):
    if(n % i == 0):
        count +=1


if count == 1:
    print("Prime")
else:
    print("Not Prime")

# fibo , pallind , armstrong ,  1, 11, 111, 1111, pattern  