class Student:
    #data members 
    # name = "" #Aman
    # age = 0 # 19

    #function -> 
    def addName(self,Newname):
     self.name = Newname

    def addAge(self,newAge):
     self.age = newAge

    def addCourse(self,newCourse):
      self.course = newCourse

    def getName(self):
      return self.name

    def welcome(self):
      print(f'Your name is {self.name} and your age is {self.age} and your course is {self.course} ')

# jitne bhi characterstices , attributes , behaviour -> us class m honge woh sab us 
#object wale variable m store hojaaenge 
s1 = Student() # object creation
s1.addName("Aman") # class function calling
s1.addAge(19)
s1.addCourse("Java Full Stack")

print(s1.getName())

# print(s1.name) # class variable display
# print(s1.age)
# print(s1.course)
# s1.welcome()


# s2 = Student()
# s2.addName("Ajay")
# s2.addAge(20)
# s2.addCourse("Python")

# print(s2.name)
# print(s2.age)
# print(s2.course)
# s2.welcome()
