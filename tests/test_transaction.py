import unittest
from src.models.transaction import Transaction
from src.services.transaction_service import TransactionService

class TestTransactionService(unittest.TestCase):

    def setUp(self):
        self.transaction_service = TransactionService()

    def test_deposit(self):
        account = self.transaction_service.create_account('Savings', 'John Doe')
        result = self.transaction_service.deposit(account, 100)
        self.assertEqual(result, 100)
        self.assertEqual(account.balance, 100)

    def test_withdraw(self):
        account = self.transaction_service.create_account('Checking', 'Jane Doe')
        self.transaction_service.deposit(account, 200)
        result = self.transaction_service.withdraw(account, 50)
        self.assertEqual(result, 150)
        self.assertEqual(account.balance, 150)

    def test_withdraw_insufficient_funds(self):
        account = self.transaction_service.create_account('Savings', 'John Doe')
        result = self.transaction_service.withdraw(account, 50)
        self.assertEqual(result, "Insufficient funds")
        self.assertEqual(account.balance, 0)

if __name__ == '__main__':
    unittest.main()