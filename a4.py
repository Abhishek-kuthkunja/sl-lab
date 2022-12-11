def ctok(temp):
    return temp+273
def ktoc(temp):
    return temp-273
def ctof(temp):
    return 1.8*temp+32
def ftoc(temp):
    return (temp-32)/1.8
def ktof(temp):
    return ctof(ktoc(temp))
def ftok(temp):
    return ctok(ftoc(temp))

while(1):
    n=int(input("enter the choice"))
    t=int(input("enter the temperature"))
    
    if n==1:
        print(ctok(t),'K')
    elif n==2:
        print(ktoc(t),'C')
    elif n==3:
        print(ctof(t),'F')
    elif n==4:
        print(ftoc(t),'C')
    elif n==5:
        print(ktof(t),'F')
    elif n==6:
        print(ftok(t),'K')
    elif n==7:
        break
        


    