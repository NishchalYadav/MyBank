from bank import Bank

import sys
import time


def print_loading():
    """Display a simple loading animation"""
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.3)
    print()


def display_menu():
    """Display the main menu options"""
    print("\n╔════ Banking System Menu ════╗")
    print("║ 1. Create Account            ║")
    print("║ 2. Check Balance             ║")
    print("║ 3. Deposit                   ║")
    print("║ 4. Withdraw                  ║")
    print("║ 5. List All Accounts         ║")
    print("║ 6. View Transactions         ║")
    print("║ 7. Exit                      ║")
    print("╚══════════════════════════════╝")


def create_account(bank):
    """Handle account creation process"""
    print("\n=== Create New Account ===")
    try:
        name = input("Enter holder name: ").strip()
        if not name:
            print("Error: Name cannot be empty!")
            return

        initial_deposit = float(input("Enter initial deposit amount: $"))
        if initial_deposit < 0:
            print("Error: Initial deposit cannot be negative!")
            return

        print("\nCreating account", end="")
        print_loading()

        acc_num = bank.create_account(name, initial_deposit)
        print(f"\nSuccess! Account created with number: {acc_num}")

    except ValueError:
        print("Error: Please enter a valid amount!")


def handle_transaction(bank, transaction_type):
    """Handle deposit or withdrawal transactions"""
    try:
        acc_num = int(input("Enter account number: "))
        account = bank.get_account(acc_num)

        if not account:
            print("Error: Account not found!")
            return

        amount = float(input(f"Enter {transaction_type} amount: $"))

        if transaction_type == "deposit":
            if account.deposit(amount):
                print("\nProcessing deposit", end="")
                print_loading()
                print("Deposit successful!")
        else:
            if account.withdraw(amount):
                print("\nProcessing withdrawal", end="")
                print_loading()
                print("Withdrawal successful!")
            else:
                print("Error: Insufficient funds!")

    except ValueError:
        print("Error: Please enter valid numbers!")


def display_accounts(accounts):
    print("\n=== Account List ===")
    print("Number    Holder              Balance")
    print("-" * 40)
    for account in accounts:
        num = account['number']
        holder = account['holder']
        balance = float(account['balance'])
        print(f"{str(num).ljust(10)}{holder.ljust(20)}${balance:.2f}")


def main():
    """Main application entry point"""
    bank = Bank("MyBank")
    print("Welcome to MyBank Banking System")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            create_account(bank)

        elif choice == "2":
            try:
                acc_num = int(input("Enter account number: "))
                account = bank.get_account(acc_num)
                if account:
                    print(f"\nCurrent balance: ${account.get_balance():.2f}")
                else:
                    print("Error: Account not found!")
            except ValueError:
                print("Error: Please enter a valid account number!")

        elif choice == "3":
            handle_transaction(bank, "deposit")

        elif choice == "4":
            handle_transaction(bank, "withdraw")

        elif choice == "5":
            accounts = bank.list_accounts()
            if not accounts:
                print("\nNo accounts found!")
            else:
                display_accounts(accounts)

        elif choice == "6":
            try:
                acc_num = int(input("Enter account number: "))
                account = bank.get_account(acc_num)
                if account:
                    transactions = account.get_transactions()
                    if transactions:
                        print("\n=== Transaction History ===")
                        for transaction in transactions:
                            print(transaction)
                    else:
                        print("No transactions found!")
                else:
                    print("Error: Account not found!")
            except ValueError:
                print("Error: Please enter a valid account number!")

        elif choice == "7":
            print("\nThank you for using MyBank!")
            print("Exiting", end="")
            print_loading()
            break

        else:
            print("Error: Invalid choice! Please try again.")


if __name__ == "__main__":
    main()