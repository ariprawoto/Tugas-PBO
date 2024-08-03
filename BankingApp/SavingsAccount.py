from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.__interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
