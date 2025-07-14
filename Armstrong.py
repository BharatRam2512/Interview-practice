n=int(input("Enter a number: "))
sum=0
a=n

while n>0:
    digit=n%10
    sum+=digit**3
    n=n//10


if sum==a:
    print(f"{a} is an Armstrong number")
else:
    print(f"{a} is not an Armstrong number")