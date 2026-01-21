import os
from abc import ABC, abstractmethod


#abstract class - Abstraction
class Account(ABC):

    def __init__(self, Account_number , owner , balance = 0):
        self.Account_number = Account_number
        self.owner = owner
        self.__balance= balance # encapsulation

    @abstractmethod
    def withdraw():
        pass

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
            print(f"Deposited {amt}. New Balance is {self.__balance}")
        else:
            print("Invalid Deposit Amount")

    def set_balance(self,new_Bal):
        self.__balance = new_Bal

    def get_balance(self):
       return self.__balance
    
    def __str__(self):
        print(f"Account Number : [{self.Account_number}] - Owner : [{self.owner}] - Balance : [{self.__balance}]")
       

#Inheritance + Polymorphism
class SavingAcc(Account): # 2000 -> 1500

    def withdraw(self,amt): # 500
        if amt <= self.get_balance():
            self.set_balance(self.get_balance - amt) # set (2000 - 500)
            print(f"Withdraw {amt} , New Balance = {self.get_balance()}")
        else:
            print("Insufficient Funds in the Savings Account")


class CurrentAccount(Account):
    def __init__(self, Account_number, owner, balance=0 , odLimit = 5000): # current k liye
        super().__init__(Account_number, owner, balance) # rest account se lekr aagya 
        self.odLimit = odLimit


    def withdraw(self,amt):
        if amt <= self.get_balance() + self.odLimit:
            self.set_balance(self.get_balance() - amt)
            print(f"Withdraw {amt} , New Balance = {self.get_balance()}")
        else:
            print("Insufficient Funds in the Current  Account")


class Customer:
    def __init__(self , name , customer_id):
        self.name = name
        self.customer_id = customer_id


    def __str__(self):
        return f"Customer : [{self.name}] - Id : [{self.customer_id}]"
    

class Bank:
    def __init__(self , filename = "accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_account()


    def createAccount(self, Account_type , account_number , owner):
        if Account_type == "Savings":
            account = SavingAcc(account_number, owner)

        elif Account_type == "Current":
            account = CurrentAccount(account_number,owner)

        else:
            print("Invalid Account Type")
            return

        self.accounts[account_number] = account
        self.save_accounts()
        print(f"{Account_type.captialize()} account is created for {owner.name}")

    def get_account(self,account_number):
            return self.accounts.get(account_number, None)
        
    def save_accounts(self):
            with open(self.filename,"w") as f:
                for acc in self.accounts.values():
                    f.write(f"{acc.Account_type}, {acc.account_number}, {acc.owner.name},{acc.owner.customer_id},{acc.getbalance()}\n")

    def load_account(self):
            if not os.path.exists(self.filename):
                return
            with open(self.filename, "r") as f:
                for line in f:
                    acc_type , acc_no , name , cust_id , balance = line.strip(),split(",")
                    owner = Customer(name,int(cust_id))

                    if acc_type == "Savings":
                        acc = SavingAcc(int(acc_no), owner , float(balance))
                    else:
                        acc = CurrentAccount(int(acc_no), owner , float(balance))

                    self.accounts[int[acc_no]] = acc


# ----- DEMO -----
if __name__ == "__main__": # all class ko ek sath run krne ka tarika 
    bank = Bank()


    while(True):
        print("\n --- BANK MENU ---")
        print("1. Create a Savings Acc")
        print("2. Create a Current Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Exit")

        choice = input("Enter your Choice: ")

        if choice == "1":
            name = input("Enter Your Customer Name \n")
            c_id = input("Enter Your Customer ID \n")
            acc_no = input("Enter Your Customer Acc No \n")
            bank.createAccount("Savings",acc_no,Customer(name,c_id) )


        elif choice == "2":
            name = input("Enter Your Customer Name \n")
            c_id = input("Enter Your Customer ID \n")
            acc_no = input("Enter Your Customer Acc No \n")
            bank.createAccount("Current",acc_no,Customer(name,c_id) )

        elif choice == "3":
            acc_no = input("Enter Your Customer Acc No")
            amount = float(input("Enter your Amount to Deposit: \n"))
            acc = bank.get_account(acc_no)

            if acc:
                acc.deposit(amount)
                bank.save_accounts()
            else:
                print("Account Not Found")

        elif choice == "4":
            acc_no = input("Enter Your Customer Acc No")
            amount = float(input("Enter your Amount to Withdraw: \n"))

            acc = bank.get_account(acc_no)

            if(acc):
                acc.withdraw(amount)
                bank.save_accounts()
            else:
                print("Account Not Found")

            
        elif choice == "5":
             acc_no = input("Enter Your Customer Acc No")
             acc = bank.get_account(acc_no)

             if acc:
                 print(f"Balance for Account {acc_no} = {acc.getBalance()}")
             else:
                 print("Account Not Found")


        elif choice == "6":
            print("Exiting... Thank Your For Banking with us!!!!")
            break

        else:
            print("Invalid Choice - Please Try Again")