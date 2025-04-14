class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute
        self.owner_name = owner_name  # Public attribute
    
    # Deposit money
    def deposit_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Withdraw money with a 1% fee
    def withdraw_money(self, amount):
        if 0 < amount <= self.__balance:
            fee = amount * 0.1  # Calculate the fee
            total_withdrawal = amount + fee  # Total amount deducted
            self.__balance -= total_withdrawal
            print(f"You withdrew {amount} with a fee of {fee}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    # Get balance
    def get_balance(self):
        return self.__balance  # Return instead of printing for flexibility

    # Set account number
    def set_account_number(self, account_number):
        self.__account_number = account_number

    # Get account number
    def get_account_number(self):
        return self.__account_number  # Return instead of printing for flexibility

    # Display balance
    def display_balance(self):
        print(f"Account balance for {self.owner_name}: {self.__balance}")


# Testing the class
bank_account1 = BankAccount(1000, "Mohamed", 1000)
bank_account1.deposit_money(500)
bank_account1.withdraw_money(200)
bank_account1.set_account_number(19950)
bank_account1.display_balance()

# Testing direct access to private attributes
try:
    print(bank_account1.__account_number)  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")