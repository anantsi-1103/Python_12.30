import os
from abc import ABC, abstractmethod

# abstract class
class Account(ABC):
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance

    @abstractmethod
    def withdraw(self, amt):
        pass

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
            print(f"Deposited {amt}. New Balance = {self.__balance}")
        else:
            print("Invalid amount")

    def get_balance(self):
        return self.__balance

    def set_balance(self, bal):
        self.__balance = bal

# account display -> 
    def __str__(self):
        return f"Account No: {self.account_number}, Owner: {self.owner.name}, Balance: {self.__balance}"

# inheritance + Polymorphism
class SavingAcc(Account):
    def withdraw(self, amt):
        if amt <= 0:
            print("Invalid amount")
        elif amt <= self.get_balance():
            self.set_balance(self.get_balance() - amt)
            print(f"Withdrawn {amt}. Balance = {self.get_balance()}")
        else:
            print("Insufficient Balance")

# inheritance + polymorphism
class CurrentAccount(Account):
    def __init__(self, acc_no, owner, balance=0, od_limit=5000):
        super().__init__(acc_no, owner, balance)
        self.od_limit = od_limit

    def withdraw(self, amt):
        if amt <= 0:
            print("Invalid amount")
        elif amt <= self.get_balance() + self.od_limit:
            self.set_balance(self.get_balance() - amt)
            print(f"Withdrawn {amt}. Balance = {self.get_balance()}")
        else:
            print("Overdraft limit exceeded")

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id


#main 
class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {} # entry hone ke baad data accounts ke andr aaega 
        self.filename = filename # filename ke andr store 
        self.load_accounts() # load account 

    def create_account(self, acc_type, acc_no, owner):
        if acc_no in self.accounts:
            print("Account already exists!")
            return

        if acc_type == "Savings":
            acc = SavingAcc(acc_no, owner)
        elif acc_type == "Current":
            acc = CurrentAccount(acc_no, owner)
        else:
            print("Invalid Account Type")
            return

        self.accounts[acc_no] = acc
        self.save_accounts()
        print(f"{acc_type} Account created successfully")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

    def save_accounts(self):
        with open(self.filename, "w") as f:
            for acc in self.accounts.values():
                acc_type = acc.__class__.__name__
                f.write(f"{acc_type}|{acc.account_number}|{acc.owner.customer_id}|{acc.owner.name}|{acc.get_balance()}\n")

    def load_accounts(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r") as f:
            for line in f:
                try:
                    acc_type, acc_no,cid, name , bal = line.strip().split("|")
                    owner = Customer(name, int(cid))

                    if acc_type == "SavingAcc":
                        acc = SavingAcc(int(acc_no), owner, float(bal))
                    else:
                        acc = CurrentAccount(int(acc_no), owner, float(bal))

                    self.accounts[int(acc_no)] = acc
                except:
                    continue


# starter -> module , background executing files unko woh run krdega -> main kaam ko execute
if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\n----- BANK MENU -----")
        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            cid = int(input("Customer ID: "))
            acc = int(input("Account No: "))
            bank.create_account("Savings", acc, Customer(name, cid))

        elif choice == "2":
            name = input("Name: ")
            cid = int(input("Customer ID: "))
            acc = int(input("Account No: "))
            bank.create_account("Current", acc, Customer(name, cid))

        elif choice == "3":
            acc = int(input("Account No: "))
            amt = float(input("Amount: "))
            acc_obj = bank.get_account(acc)
            if acc_obj:
                acc_obj.deposit(amt)
                bank.save_accounts() # file m changes
            else:
                print("Account not found")

        elif choice == "4":
            acc = int(input("Account No: "))
            amt = float(input("Amount: "))
            acc_obj = bank.get_account(acc)
            if acc_obj:
                acc_obj.withdraw(amt)
                bank.save_accounts()
            else:
                print("Account not found")

        elif choice == "5":
            acc = int(input("Account No: "))
            acc_obj = bank.get_account(acc)
            if acc_obj:
                print("Balance:", acc_obj.get_balance())
            else:
                print("Account not found")

        elif choice == "6":
            print("Thank you for banking!")
            break

        else:
            print("Invalid choice")
