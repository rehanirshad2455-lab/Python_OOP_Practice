class student:
    def __init__(self , name , marks):
        self.__name = name
        self.__marks = 0
        self.set_marks(marks) 

    def set_marks(self,marks):
        if self.__marks >= 0 and self.__marks <= 100:
            self.__marks = marks    
        else:
            print("Invalid marks!")

    def getter(self):
            return self.__marks

    def display_info(self):
        print("Name : ", self.__name)
        print("Marks : ", self.__marks)

s1 = student("Rehan", 50)
s1.display_info()

