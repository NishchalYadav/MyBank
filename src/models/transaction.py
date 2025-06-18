class Transaction:
    def __init__(self, amount, transaction_type, account):
        self.amount = amount
        self.transaction_type = transaction_type
        self.account = account

    def execute(self):
        if self.transaction_type == 'deposit':
            self.account.deposit(self.amount)
        elif self.transaction_type == 'withdrawal':
            self.account.withdraw(self.amount)
        else:
            raise ValueError("Invalid transaction type")

    def __str__(self):
        return f"{self.transaction_type.capitalize()} of {self.amount} on account {self.account.account_number}"