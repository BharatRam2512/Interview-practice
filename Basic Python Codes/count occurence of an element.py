str=input("enter a string: ")
x=input("enter an element to search: ")
count=0
for char in str:
    if char==x:
        count+=1
print(f"The search element {x} found {count} times")