class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdraw amount or insufficient funds")

    def get_balance(self):
        return self.__balance

    def get_account_details(self):
        return f"Account Number: {self.__account_number}, Account Holder: {self.__account_holder}, Balance: {self.__balance}"
