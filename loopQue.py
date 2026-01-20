# sum , factorial -> 
# pallindrome , armstrong -> 
# fibo , 1, 11, 111, patterns -> 

def isArmstrong(n): # 234
    temp = n # 234 23 2
    sum = 0 # 0 64 91 99

    while(temp != 0): #T T TF
        #extract
        digit = temp % 10 # 2
        #sum - store
        sum = sum + digit ** 3 # 91 + 8 = 99
        #short
        temp = temp // 10 # 0

    if(sum == n):
        return True
    
    else:
        return False

def isPallindrome(n): # 142
    temp = n # 142 14 1
    sum = 0 # 0 2 24 241
    
    while(temp != 0): # T T T F
        #extract
        digit = temp % 10 # 1 - 1
        #sum - store
        sum = sum * 10 + digit # 24 * 10 + 1 = 241
        #short
        temp = temp // 10 # 0 142 - 14 - 1 - 0

    if(sum == n):
        return True
    
    else:
        return False

# fibonacci series -> normal loop , recursion ->
def fibonacci(n):
    a = 0
    b = 1

    print(a,end=" ")
    print(b,end=" ")

    for i in range(2,n+1):
        c = a+b
        print(c,end=" ")

        a = b
        b = c

# 1,11,111,1111
def series(n):
    d = 1

    for i in range(1, n+1):
        print(d,end=" ")
        d = d * 10 + 1

def sqaurePattern(n):

    #outer -> 0 - 4
    for i in range(n):
        for j in range(n):
             #display -> data ko same line m rkh rhe ho
            print("*" , end=" ")
        print()

def rightAngleStar(n):
    for i in range(1,n+1):
        for j in range(i):
             print("*" , end=" ")
        print()

def rightAngleNum(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
             print(j , end=" ")
        print()

def rightAngleWord(n):
    for i in range(1,n+1):
        ch = 'A'
        for j in range(1,i+1):
             print(ch , end=" ")
             ch = chr(ord(ch)+1)
        print()

def floydTriangle(n):
    c = 1
    for i in range(1,n+1): # 4
        for j in range(i): # 1 2 3 4
             print(c , end=" ")
             c+=1 # 7
        print()
