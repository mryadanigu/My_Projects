class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        self.balance += amount
        print(f"Successfully deposited ${amount:.2f}. Your new balance is ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Successfully withdrew ${amount:.2f}. Your new balance is ${self.balance:.2f}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_number, account_holder, initial_balance=0):
        if account_number in self.accounts:
            print("Account number already exists.")
            return
        self.accounts[account_number] = BankAccount(account_number, account_holder, initial_balance)
        print(f"Account {account_number} opened for {account_holder} with balance ${initial_balance:.2f}")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer_funds(self, from_account, to_account, amount):
        from_acc = self.get_account(from_account)
        to_acc = self.get_account(to_account)

        if not from_acc or not to_acc:
            print("One or both accounts do not exist.")
            return
        
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        
        if from_acc.balance < amount:
            print("Insufficient funds in the from account.")
            return
        
        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        print(f"Successfully transferred ${amount:.2f} from account {from_account} to account {to_account}")

def bank_interface():
    bank = Bank()
    print("\nWelcome to the Bank System.")

    while True:
        print("\n[*] Please select an option:")
        print(" 1. Open an account")
        print(" 2. Check balance")
        print(" 3. Deposit")
        print(" 4. Withdraw")
        print(" 5. Transfer funds")
        print(" 6. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == "1":
            account_number = input("Enter a new account number: ")
            account_holder = input("Enter the account holder's name: ")
            initial_balance = float(input("Enter initial balance (0 if none): "))
            bank.open_account(account_number, account_holder, initial_balance)
        elif choice == "2":
            account_number = input("Enter the account number: ")
            account = bank.get_account(account_number)
            if account:
                print(f"Balance for account {account_number}: ${account.check_balance():.2f}")
            else:
                print("Account not found.")
        elif choice == "3":
            account_number = input("Enter the account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found.")
        elif choice == "4":
            account_number = input("Enter the account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == "5":
            from_account = input("Enter the sender's account number: ")
            to_account = input("Enter the receiver's account number: ")
            amount = float(input("Enter the amount to transfer: "))
            bank.transfer_funds(from_account, to_account, amount)
        elif choice == "6":
            print("Thank you for using the Bank System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    bank_interface()
