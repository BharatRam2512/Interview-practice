n= int(input("enter a number: "))
sum=0
a=n
while n!=0:
    digit =n%10
    sum=sum*10+digit
    n=n//10

print(f"reverse of {n} is {sum}")