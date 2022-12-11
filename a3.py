class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length * self.breadth
    
a=int(input("enter the length"))
b=int(input("enter the breadth"))
obj=rectangle(a,b)

print("area is",obj.area())