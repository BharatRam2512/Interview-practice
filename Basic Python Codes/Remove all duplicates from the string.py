str=input("enter a string: ")
x=""
for char in str:
    if char not in x:
        x+=char
print(f"String after removing duplicates: {x}")