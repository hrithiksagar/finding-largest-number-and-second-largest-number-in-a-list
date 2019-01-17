#3)finding a largest number in a list
list=[]
s=int(input("input the size of list"))
for i in range(s):
    x=int(input("enter list items"))
    list.append(x)
    n=list[0]
if (list[i]>n):
    n=list[i]    
print("max[list]",n)  




#4)finding second largest number in the list
list=[]
s=int(input("input the size of list"))
for i in range(s):
    x=int(input("enter list items"))
    list.append(x)
    
list.sort()
print("second largest element",list[-2])
