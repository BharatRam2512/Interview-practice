a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))

if a>b:
    if a>c:
        print(f"a= {a} is the largest number")
    else:
        print(f"c= {c} is the largest number")
else:
    if b>c:
        print(f"b= {b} is the largest number")
    else:
        print(f"c= {c} is the largest number")