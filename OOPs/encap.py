class BankAccount:

# data hidden and safe
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amt):
        self.__balance += amt

    def showBalance(self):
        print("Balance is", self.__balance)

bk = BankAccount(10000)

bk.deposit(2000)
bk.deposit(6000)
bk.deposit(8000)

bk.showBalance()

