class Parent:
    def property_Par(self):
        print("1000 Gaj")


class Child(Parent): 
    def property_Child(self):
        print("500 Gaj")

    def display(self):
        print("Property of Child")
        


c = Child()

c.property_Child()
c.display()

c.property_Par()