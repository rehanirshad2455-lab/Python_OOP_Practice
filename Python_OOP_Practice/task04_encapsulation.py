class bankAccount:
    def __init__(self , balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited " , amount)
        else:
            print("Invalid amount : ")

    def widthraw(self , amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn : " , amount)
        else:
            print("Invalid withdrawal : ")

    def current_balance(self):
        print("Your current balance is : ",self.__balance)

acc = bankAccount(500)
acc.deposit(500)
acc.widthraw(500)
acc.current_balance()