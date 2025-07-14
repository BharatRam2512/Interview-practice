n=int(input("Enter a number: "))
sum=0
a=n
while n>0:
    digit =n%10
    sum=sum+digit
    n=n//10

print(f"sum of digits of {a} is {sum}")




#method 2
x=0
for i in str(a):
    x+=int(i)

print(f"sum of digits in {a} is {sum}")