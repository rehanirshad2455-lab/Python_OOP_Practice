class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My Name is" , self.name , "I am" , self.age , "years old")

class Employee(person):
    def __init__(self, name, age , empId , salary):
        super().__init__(name, age)
        self.empId = empId
        self.salary = salary

    def show(self):
        print("Employee id is :" , self.empId , "Salary of employee is ", self.salary)

class Teacher(Employee):
    def __init__(self , name , age ,empId ,salary,  subject ,expYears):
        super().__init__(name , age,empId,salary)
        self.subject = subject
        self.expYears = expYears

    def teach(self):
        print("Sir Ahmad is teaching " ,self.subject, "with" , self.expYears, " years of experience")


t1 = Teacher("Ahmad" , 25 ,505, 8000, "Python", 12)
t1.introduce()
t1.show()
t1.teach()
    