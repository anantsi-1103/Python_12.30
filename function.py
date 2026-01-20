# function declaration - creation 
def hello():
    for i in range(1,n+1):
        print('hello')

# always -> block -> isEven -> 
def isEven(n):
    if(n % 2 == 0):
        print("Even")
    else:
        print("Odd")


# gift ->  normal
def sum_print(a,b):
    print(a+b)
    
#  money ->  integer function
def sum_return(a,b):
    return a+b

#boolean function 
def ischeck(n):
    if(n >= 18):
        return True
    else:
        return False
    

# String function
def ischeck_String(n):
    if(n >= 18):
        return "allowed"
    else:
        return "Not Allowed"
     


# indepdently -> no loop , no condition , no logic - just a alone function name
#hello name ka function hoga -> nhi hoga -> function is not declared 
# function helps in code reusability -> 
