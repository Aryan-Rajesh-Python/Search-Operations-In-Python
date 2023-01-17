n=int(input("Enter the length of the list: "))
lst=[]
for i in range(n):
    values=int(input(f"Enter the {i+1}th element: "))
    lst.append(values)
print(lst)
def linear():
    a=int(input("Enter the number to be searched: "))
    def find(lst,a):
        position=0
        while(position<len(lst)):
            if(lst[position]==a):
                return position
            position+=1
        return -1
    result=find(lst,a)
    if(result==-1):
        print(f"{a} is not present in the list")
    else:
        print(f"{a} is found at the {result}th position in the list")
def binary():
    a=int(input("Enter the number to be searched: "))
    def locate(lst,a):
        low=0
        high=len(lst)-1
        while(low<=high):
            mid=(low+high)//2
            if(lst[mid]==a):
                return mid
            elif(lst[mid]<a):
                low=mid+1
            elif(lst[mid]>a):
                high=mid-1
        return -1
    result=locate(lst,a)
    if(result==-1):
        print(f"{a} is not present in the list")
    else:
        print(f"{a} is found at the {result}th position in the list")
while(True):
    choice=input("Enter the search you want to perform: ")
    if(choice=="linear"):
        linear()
    elif(choice=="binary"):
        binary()
    else:
        print("Thank you for using our search application!")
        break