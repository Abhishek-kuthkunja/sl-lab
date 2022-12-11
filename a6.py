def AtomicDictionary():
    name={'s':'sulphur','c':'carbon','h':'hydrogen','o':'oxygen'}
    add=input("enter the element symbol")
    add1=input("enetr its name")
    name[add]=add1
    print(name)
    add=input("enter the element symbol")
    add1=input("enetr its name")
    name[add]=add1
    print(name)
    print(len(name))
    serach=input('enter the element to serach')
    if serach in name:
        print("eleemnt is exit")
    else:
        print("eleemnt is not there")

