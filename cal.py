class caluclation:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def Area(self):
        print(f"Area of Rectangle:{self.length*self.breadth}")
    def Perimeter(self):
        print(f"Perimeter of Rectangle:{2*(self.length*self.breadth)}")
c=caluclation(2,4)
c.Area()
c.Perimeter()

        