import unittest
from src.models.account import SavingsAccount, CheckingAccount

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.savings_account = SavingsAccount(account_number="123456", balance=1000)
        self.checking_account = CheckingAccount(account_number="654321", balance=500)

    def test_deposit(self):
        self.savings_account.deposit(500)
        self.assertEqual(self.savings_account.balance, 1500)

    def test_withdraw(self):
        self.checking_account.withdraw(200)
        self.assertEqual(self.checking_account.balance, 300)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.checking_account.withdraw(600)

    def test_display_details(self):
        details = self.savings_account.display_details()
        self.assertIn("Account Number: 123456", details)
        self.assertIn("Balance: 1000", details)

    def test_to_dict(self):
        account_dict = self.savings_account.to_dict()
        self.assertEqual(account_dict['account_number'], "123456")
        self.assertEqual(account_dict['balance'], 1000)

if __name__ == '__main__':
    unittest.main()