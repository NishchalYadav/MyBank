def validate_account_number(account_number):
    if not isinstance(account_number, str) or len(account_number) != 10 or not account_number.isdigit():
        raise ValueError("Account number must be a 10-digit string.")

def validate_amount(amount):
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Amount must be a positive number.")

def validate_transaction_type(transaction_type):
    valid_types = ['deposit', 'withdrawal']
    if transaction_type not in valid_types:
        raise ValueError(f"Transaction type must be one of: {', '.join(valid_types)}.")

def validate_customer_name(name):
    if not isinstance(name, str) or len(name) == 0:
        raise ValueError("Customer name must be a non-empty string.")