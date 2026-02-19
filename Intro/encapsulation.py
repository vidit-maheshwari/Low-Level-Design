class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def check_balance(self):
        return self.__balance
    

if __name__ == "__main__":
    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Current balance: {account.check_balance()}")