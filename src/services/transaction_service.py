from models.transaction import Transaction
from models.account import Account

class TransactionService:
    def deposit(self, account: Account, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        account.balance += amount
        print(f"Deposited {amount} to account {account.account_number}. New balance: {account.balance}")

    def withdraw(self, account: Account, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > account.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        account.balance -= amount
        print(f"Withdrew {amount} from account {account.account_number}. New balance: {account.balance}")

    def transfer(self, from_account: Account, to_account: Account, amount: float) -> None:
        self.withdraw(from_account, amount)
        self.deposit(to_account, amount)
        print(f"Transferred {amount} from account {from_account.account_number} to account {to_account.account_number}.")