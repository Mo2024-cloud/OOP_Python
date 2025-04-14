class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.__account_number = account_number
        self.__balance = balance
        self.owner_name = owner_name
    
    #Setter Method to deposit money
    def deposit_money(self, balance):
        if balance > 0:
            self.__balance+= balance
            print(f"Deposited {balance}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    #Getter Method to withdraw money
    def withdraw_money(self, balance):
        if 0 < balance <= self.__balance:
            self.__balance-= balance
            print(f"You withdraw {balance} and Your amount now is {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    #Getter For Balance
    def get_balance(self):
        print(f"The Balance is {self.__balance}") 

    #Setter Account Number
    def set_acount_number(self, account_number):
        self.__account_number = account_number

    #Getter Account Number
    def get_account_number(self):
        print(f"The Acount Number is {self.__account_number}") 

    # Method to display balance
    def display_balance(self):
        print(f"Account balance for {self.owner_name}: {self.__balance}")

bank_account1 = BankAccount(1000, "Mohamed")
bank_account1.deposit_money(500)
bank_account1.withdraw_money(200)
bank_account1.set_acount_number(19950)
bank_account1.display_balance()
