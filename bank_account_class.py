class BankAccount:
    def __init__(self, account_number: str, owner_name: str):
        # Initializes fields: account_number, owner_name, balance (starts at 0)
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = 0

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if self.balance > amount:
            self.balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self.balance


if __name__ == "__main__":
    account = BankAccount("123456", "John Doe")
    account.deposit(1000)
    print(account.get_balance())  # Should print 1000.0

    success = account.withdraw(500)
    print(str(success).lower())  # Should print true
    print(account.get_balance())  # Should print 500.0

    success = account.withdraw(1000)
    print(str(success).lower())  # Should print false
