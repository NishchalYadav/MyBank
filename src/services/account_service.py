from src.models.account import SavingsAccount, CheckingAccount

class AccountService:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type, account_holder, initial_balance=0):
        if account_type == 'savings':
            account = SavingsAccount(account_holder, initial_balance)
        elif account_type == 'checking':
            account = CheckingAccount(account_holder, initial_balance)
        else:
            raise ValueError("Invalid account type. Choose 'savings' or 'checking'.")
        
        self.accounts[account.account_number] = account
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
            return True
        return False

    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            return account.withdraw(amount)
        return False

    def display_account_details(self, account_number):
        account = self.get_account(account_number)
        if account:
            return account.display_details()
        return None