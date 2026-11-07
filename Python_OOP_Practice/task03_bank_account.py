class bankAccount:
    def __init__(self , account_holder , balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def widthraw(self , amount):
        self.balance -= amount

    def current_balance(self):
        print("Account Holder : " , self.account_holder)
        print("Your current balance is : ",self.balance)

acc = bankAccount("Rehan Irshad",500)
acc.deposit(500)
acc.widthraw(500)
acc.current_balance()