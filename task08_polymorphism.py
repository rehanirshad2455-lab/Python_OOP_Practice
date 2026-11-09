class Parent:
    def __init__(self , name ):
        self.name = name

    def getPayment(self):
        print("Not defined")

class Student(Parent):
    def __init__(self, name , fee):
        super().__init__(name)
        self.fee = fee
    def getPayment(self):
        print(f"{self.name} (Student) has to pay fee: {self.fee}")

class Teacher(Parent):
    def __init__(self, name , salary):
        super().__init__(name)
        self.salary = salary

    def getPayment(self):
        print(f"{self.name} (Teacher) receives salary: {self.salary}")

class staff(Parent):
    def __init__(self, name , daily_wages , daily_worked):
        super().__init__(name)
        self.daily_wages = daily_wages
        self.daily_worked = daily_worked

    def getPayment(self):
        total = self.daily_wages * self.daily_worked
        print(f"{self.name} (Staff) earns total wage: {total}")


if __name__ == "__main__":
    people = [
        Student("Rehan Irshad" , 150000),
        Teacher("Sir Ahmad" , 200000),
        staff("Bilal" , 600 , 20),

    ]

    for p in people:
        p.getPayment()
        
