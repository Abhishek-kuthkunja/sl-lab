n=int(input("enter the number of element"))
li=[]
for i in range(n):
    y=int(input("eelemt"))
    li.append(y)
print(li)
li.insert(1,10)#insert
print(li)
li.remove(2)#remove
print(li)
z=li.count(10)#count the number
if z==0:
    print("element is not there")
elif z>0:
    print("element is present")
li.sort()
print(li[len(li)-1],"max ele")#max element
print(li[0])#min element
