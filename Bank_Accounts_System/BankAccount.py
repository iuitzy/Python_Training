class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = initial_balance  # Encapsulated balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance

    def display_account_details(self):
        print(f"Account Number: {self.account_number}, Holder: {self.account_holder}, Balance: {self.__balance}")

# Example usage
def main():
    account = BankAccount("123456", "John Doe", 1000)
    account.display_account_details()
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)  # Should show insufficient balance
    print("Final Balance:", account.get_balance())

if __name__ == "__main__":
    main()