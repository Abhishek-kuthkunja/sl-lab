from functools import reduce
list1=[]
print("enter 6 number to add to the list")
for i in range(6):
    num=int(input())
    list1.append(num)
    
print("the list is",list1)

list2=[i*3 for i in list1]
print("the new list is",list2)

sum1=reduce(lambda x,y :x+y,list1)
sum2=reduce(lambda x,y:x+y,list2)

print(sum1)
print(sum2)    