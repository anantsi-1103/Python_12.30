class Father:
    def speak(self):
        print("Father Speaking")

class Mother:
    def eat(self):
        print("Mother Eating")



class Child(Father,Mother):
    def sleep(self):
        print("Child Sleeping")



c = Child()
c.eat()
c.sleep()
c.speak()