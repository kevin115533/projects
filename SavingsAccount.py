class SavingsAccount(object):
    RATE = 0.02

    def __init__(self, name, pin, balance = 0.0):
        self._name = name
        self._pin = pin
        self._balance = balance

    def __str__(self):
        result = "Name:    " + self._name + "\n"
        result += "PIN:     " + self._pin + "\n"
        result += "Balance: " + str(self._balance)
        return result

    
    def getBalance(self):
        return self._balance

    def getName(self):
        return self._name

    def getPin(self):
        return self._pin

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        elif self._balance < amount:
            return "Insufficient funds"
        else:
            self._balance -= amount
            return None

    def computeInterest(self):
        interest = self._balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

class Bank(object):
    def __init__(self):
        self._accounts = {}

    def __str__(self):
        return "\n".join(map(str, self._accounts.values()))

    def add(self, account):
        self._accounts[account.getPin()] = account

    def remove(self, pin):
        return self._accounts.pop(pin, None)

    def get(self, pin):
        return self._accounts.get(pin, None)

    def computeInterest(self):
        total = 0.0
        for account in self._accounts.values():
            total += account.computeInterest()
            return total
