import json
import random

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. Current balance: ${self.balance}")
        else:
            print("Invalid amount. It should be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance: ${self.balance}")
        else:
            print("Invalid amount or insufficient balance.")

    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from()

    def create_account(self, name, initial_deposit):
        account_number = random.randint(100000, 999999)
        while account_number in self.accounts:
            account_number = random.randint(100000, 999999)

        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to()
        print(f"Account has been created! Your account number is {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account number: {account.account_number}\nName: {account.name}\nBalance: ${account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to()
        else:
            print("Account not found.")

    def save_to(self):
        with open(self.filename, "w") as file:
            json.dump({acc: acc_obj.to_dict() for acc, acc_obj in self.accounts.items()}, file)

    def load_from(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.accounts = {int(acc): Account(acc_obj["account_number"], acc_obj["name"], acc_obj["balance"]) for acc, acc_obj in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            print("No previous data found. Starting fresh.")

def main():
    bank = Bank()

    while True:
        print("\nBanking System:")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Initial deposit: "))
            bank.create_account(name, initial_deposit)

        elif choice == "2":
            account_number = int(input("Enter account number: "))
            bank.view_account(account_number)

        elif choice == "3":
            account_number = int(input("Account number: "))
            amount = float(input("Amount: "))
            bank.deposit(account_number, amount)

        elif choice == "4":
            account_number = int(input("Account number: "))
            amount = float(input("Amount: "))
            bank.withdraw(account_number, amount)

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()