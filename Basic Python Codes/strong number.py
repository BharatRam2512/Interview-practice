n=int(input("enter a number: "))

def fact(r):
    if r==1:
        return 1
    else:
        return fact(r-1)*r

r=1
sum=0
a=n
while(n!=0):
    r=n%10
    sum+=fact(r)
    n=n//10
if a==sum:
    print(f" {a} is a storng number")
else:
    print(f" {a} is not a strong number")