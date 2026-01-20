from abc import ABC, abstractmethod


class BankAccount(ABC):

    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def checkBalance(self):
        pass


class Account(BankAccount):

    def __init__(self , bal):
       self.balance = bal

    def deposit(self, amount):
      self.balance += amount
      print(f"Deposited Amount {amount}")

    def withdraw(self, amount):
      if amount <= self.balance:
         self.balance -= amount
         print(f"Withdraw Amount {amount}")
      else:
         print("Insufficient Balance")

    def checkBalance(self):
       print(f"Current Balance is {self.balance}")



acc = Account(10000)

acc.deposit(3000)
acc.withdraw(1500)
acc.checkBalance()