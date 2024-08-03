from BankAccount import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.__overdraft_limit:
            self._BankAccount__balance -= amount
        else:
            print("Invalid withdraw amount or exceeds overdraft limit")
