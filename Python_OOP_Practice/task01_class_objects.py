class student:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name : " ,self.name)
        print("Age : " , self.age)

s1 = student("Rehan Irshad" , 18)
s1.display_info()