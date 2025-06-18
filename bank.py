# bank.py
from account import Account

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    
    def create_account(self, holder_name, initial_deposit):
        account_number = len(self.accounts) + 1001
        self.accounts[account_number] = Account(holder_name, initial_deposit)
        return account_number
    
    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        return None
        
    def list_accounts(self):
        accounts_info = []
        for account_num, account in self.accounts.items():
            accounts_info.append({
                'number': account_num,
                'holder': account.holder,
                'balance': float(account.get_balance())
            })
        return accounts_info