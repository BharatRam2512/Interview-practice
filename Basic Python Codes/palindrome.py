n=int(input("Enter a number: "))
sum=0
a=n
while n!=0:

    digit =n%10
    sum=sum*10+digit
    n=n//10

if sum ==a:
    print(f"{a} is a palindrome")
else:

    print(f"{a} is not a palindrome")