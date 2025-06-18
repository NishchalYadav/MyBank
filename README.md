# README.md

# Banking System Console Application

This project is a console-based Banking System application that simulates customer account management. It includes features such as account creation, deposits, withdrawals, and interest application, all while utilizing Object-Oriented Programming principles.

## Features

- Account Creation
- Deposit and Withdrawal Management
- Interest Application
- Customer Account Management

## Project Structure

```
banking-system
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── account.py
│   │   ├── customer.py
│   │   └── transaction.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── account_service.py
│   │   └── transaction_service.py
│   └── utils
│       ├── __init__.py
│       ├── validators.py
│       └── constants.py
├── tests
│   ├── __init__.py
│   ├── test_account.py
│   └── test_transaction.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd banking-system
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.