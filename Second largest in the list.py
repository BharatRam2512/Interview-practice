lst=list(map(int, input("enter numbers: ").split(" ")))
def second_largest(lst):
    x=set()
    for i in lst:
        if i not in x:
            x.add(i)
    x=sorted(x)
    print(x)
    return x[-2] 
print(f"Second largest number in the list is: {second_largest(lst)}")

