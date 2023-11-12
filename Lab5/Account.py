class Account:
    def __init__(self, first_name, last_name, account_number, rate):
        self._account_balance = 0
        self._account_number = account_number
        self._account_first_name = first_name
        self._account_last_name = last_name
        self._rate = rate

    def deposit(self, value):
        if value > 0:
            self._account_balance += value
        else:
            raise ValueError("You can't deposit a negative value in your account")

    def withdraw(self, value):
        pass

    def get_balance(self):
        return f"Your balance: {self._account_balance}"

    def interest_calculation(self):
        interest = self._account_balance * self._rate
        return interest


class SavingsAccount(Account):
    def __init__(self, first_name, last_name, account_number, limit, rate):
        super().__init__(first_name, last_name, account_number, rate)
        self._limit = limit

    def withdraw(self, value):
        if 0 < value <= self._account_balance and value <= self._limit:
            self._account_balance -= value
        else:
            raise ValueError("Insufficient funds for withdrawal or exceeding limit")


class CheckingAccount(Account):
    def __init__(self, first_name, last_name, account_number, rate):
        super().__init__(first_name, last_name, account_number, rate)

    def withdraw(self, value):
        if 0 < value <= self._account_balance:
            self._account_balance -= value
        else:
            raise ValueError("Insufficient funds for withdrawal")


ch = CheckingAccount("ana", "ioana", 123, 0.05)
ch.deposit(5)
print(ch.get_balance())
# ch.withdraw(7)

sa = SavingsAccount("Ana", "Maria", 125, 100, 0.10)
sa.deposit(1000)
sa.withdraw(10)
# print(sa.get_balance())
# sa.deposit(-100)
