class Account:
    def __init__(self, holder_name, initial_balance):
        self.holder = holder_name
        self.balance = float(initial_balance)
        self.transactions = []
        # Record initial deposit
        self.transactions.append({
            'type': 'deposit',
            'amount': initial_balance,
            'balance': initial_balance
        })
    
    def get_balance(self):
        return float(self.balance)

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({
            'type': 'deposit',
            'amount': amount,
            'balance': self.balance
        })

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            # Record withdrawal transaction
            self.transactions.append({
                'type': 'withdrawal',
                'amount': amount,
                'balance': self.balance
            })
            return True
        return False

    def display_details(self):
        return f"Account Holder: {self.holder}, Balance: {self.balance}"

    def to_dict(self):
        return {
            "holder_name": self.holder,
            "balance": self.balance
        }

    def get_transactions(self):
        return self.transactions


class SavingsAccount(Account):
    def __init__(self, holder_name, initial_balance, interest_rate):
        super().__init__(holder_name, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        # Record interest application as a transaction
        self.transactions.append({
            'type': 'interest',
            'amount': self.balance * self.interest_rate,
            'balance': self.balance
        })


class CheckingAccount(Account):
    def __init__(self, holder_name, initial_balance, overdraft_limit):
        super().__init__(holder_name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            # Record withdrawal transaction
            self.transactions.append({
                'type': 'withdrawal',
                'amount': amount,
                'balance': self.balance
            })
            return True
        return False