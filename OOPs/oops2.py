class Car:

    # model , name  - data member

# constructor automatically run kr rha hai
    def __init__(self,name,model):
        print("Inside Constructor")
        self.name = name
        self.model = model

    # def __init__(self):
    #     print("No Argument Constructor")


    # def addCarName(self,name , model):
    #     self.name = name
    #     self.model = model

    def data(self):
        print(f"Your Car name is {self.name} and model is {self.model}")

    def getCarName(self):
        return self.name,self.model
    
# object create -> constructor 
c1 = Car("Verna" , "top")

c1.data()


# c1.addCarName("Verna" , "Top")
# print(c1.getCarName())