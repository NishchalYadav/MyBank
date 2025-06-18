class Customer:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number

    def display_details(self):
        return f"Customer Name: {self.name}, Account Number: {self.account_number}"