class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.__balance:
            print(f"Error: Insufficient funds. Balance: ${self.__balance}")
        else:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
    
    def get_balance(self):
        return self.__balance


account = BankAccount(1000)  

print(f"Initial balance: ${account.get_balance()}")


account.deposit(500)
print(f"Balance after deposit: ${account.get_balance()}")

account.withdraw(200)
print(f"Balance after withdrawal: ${account.get_balance()}")


print("\nAttempting invalid withdrawal:")
account.withdraw(1500)  

print(f"\nFinal balance: ${account.get_balance()}")


print("\n--- Testing more invalid operations ---")
account.withdraw(-50)  
account.deposit(-100)  