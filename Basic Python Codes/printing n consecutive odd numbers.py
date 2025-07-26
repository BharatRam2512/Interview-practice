n=int(input("enter a number:"))
start=int(input("enter a number: "))

if start%2==0:
    start+=1

for i in range(n):      
    print(start+2*i, end=" ")  