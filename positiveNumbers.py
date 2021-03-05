list1=[]
list2=[]
length=int(input("Enter number of elements in the list "))
print("Input the numbers in the list: ")
for i in range(0,length):
    list1.append(int(input()))
for num in list1:
    if num>0:
        list2.append(num)
print("The positive numbers in the range are: ",list2)
