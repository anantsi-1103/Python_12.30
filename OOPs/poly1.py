# print(len("Demo")) # len - String
# print(len([1,23,4,2,34,7])) # len - List
# print(len((1,2,32,3,4,3))) # len - tuple

# operator overloading 
# print("Aman"+"Singh") # string - concat 
# print(10+20) # int - add
# print([102,34,23]+[55,66,53]) # merge 

# class Cal:  
#     def cal(self,a,b):
#         return a+b
    

#     def cal(self,a,b,c):
#         return a+b+c


#     def cal(self,a,b,c,d):
#         return a+b+c+d
    

# c = Cal()
# c.cal(10,20)


# class Cal:
#     def add(self, a, b =0 , c = 0):
#         return a+b+c
    


# c = Cal()
# print(c.add(10))
# # b= 55 , a = 10 , c = 0
# print(c.add(10,55))
# print(c.add(10,55,87))

class Parent:
    def speak(self):
        print("Hindi from Parent")


class Child(Parent):
    def demo(self):
        print("Demo from Child")

    def speak(self):
        print("English")



c = Child()
c.demo()
c.speak()

