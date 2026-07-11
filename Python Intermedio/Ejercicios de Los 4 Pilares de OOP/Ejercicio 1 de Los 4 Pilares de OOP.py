class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, minimum_balance=0):
        super().__init__(balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance - self.minimum_balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive and leave sufficient funds for the minimum balance.")

    def get_balance(self):
        return self.balance

# Example usage:
if __name__ == "__main__":

    account = SavingsAccount(balance=1000, minimum_balance=100)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500)  # This should fail due to minimum balance constraint
    print(f"Final balance: {account.get_balance()}")