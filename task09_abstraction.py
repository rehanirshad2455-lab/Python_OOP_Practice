from abc import ABC,abstractmethod
class bankAccount(ABC):
    def __init__(self , holder_name , balance):
        self.holder_name = holder_name
        self.balance = balance

    def show_balance(self):
        print(f"{self.holder_name} | Balance: {self.balance}")

    @abstractmethod
    def calculate_interest():
        pass

    @abstractmethod
    def account_type():
        pass

class saving_Account(bankAccount):
    def calculate_interest(self):
        return self.balance * 0.05

    def account_type(self):
        return "savings"

class current_account(bankAccount):
    def calculate_interest(self):
        return 0

    def account_type(self):
        return "current account"

try:
    test = bankAccount("Test", 1000)
except TypeError as e:
    print("Error:", e)

acc1 = saving_Account("Rehan", 100000)
print("Account type:", acc1.account_type())
acc1.show_balance()
print("Interest:", acc1.calculate_interest())

acc2 = current_account("Ali", 50000)
print("Account type:", acc2.account_type())
acc2.show_balance()
print("Interest:", acc2.calculate_interest())