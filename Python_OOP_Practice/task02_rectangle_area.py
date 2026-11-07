class rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def calc_Area(self):
        Area = self.length * self.width
        return Area

    def calc_Parameter(self):
        parameter = 2 * (self.length + self.width)
        return parameter

    def display_info(self):
        print("Area of Rectangle :", self.calc_Area())
        print("Parameter of ractangle : " ,self.calc_Parameter())

rec = rectangle(5 , 5)
rec.display_info()

    