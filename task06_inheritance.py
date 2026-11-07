class Person:
    """Parent class: common data and behaviour."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


class Student(Person):
    """Child class: gets everything from Person, adds its own."""

    def __init__(self, name, age, roll_no):
        super().__init__(name, age)  # parent ka constructor call
        self.roll_no = roll_no

    def study(self):
        print(f"{self.name} is studying.")


class Teacher(Person):
    """Another child class of Person."""

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")


if __name__ == "__main__":
    student = Student("Rehan", 20, 101)
    teacher = Teacher("Sir Ahmed", 40, "Python")

    print("--- Student ---")
    student.introduce()  # Person se mila hua method
    print(f"Roll No : {student.roll_no}")
    student.study()

    print("--- Teacher ---")
    teacher.introduce()  # Person se mila hua method
    print(f"Subject : {teacher.subject}")
    teacher.teach()