import math #importing external modules
#class declaration
class Hello:
    #class variables declaration
    def __init__(self):
        #instance variables declaration
        pass
    def hell(self):
        #instance method declaration
        print("hello",end=" ")
    @classmethod
    def hell1(cls):
        #class method declaration
        print("world")
    @staticmethod
    def hell2():
        #static method declaration
        print("mani",math.sqrt(2))#using math module print sqrt N
#driver code
#Hello object instantiation
h=Hello()
#calling instance method 
h.hell()
#calling class method
Hello.hell1()
#calling static method
Hello.hell2()

