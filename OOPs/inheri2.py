class Animal:
    def breathe(self):
        print("breathing")


#Single
class Dog(Animal):
    def speak(self):
        print("Bark")


#multi level
class BabyDog(Dog):
    def eat(self):
        print("eating")


class Cat(Animal):
    def speak(self):
        print("Meow")



d = BabyDog()
d.breathe()
d.speak()
d.eat()