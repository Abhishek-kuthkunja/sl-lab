class student:
    li=[]
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def accept(self):
        self.name=input("enter the name")
        self.age=input("enter the age")
        for i in range(3):
            x=int(input("enter the mark"))
            self.li.append(x)
            
    def describe(self):
        print("name is",self.name,"age is",self.age)
        print("marks is",self.li)
        
stud=student(' ',' ')
stud.accept()
stud.describe()




        
    