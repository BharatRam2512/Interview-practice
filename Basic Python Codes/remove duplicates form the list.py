lst=list(map(int, input("enter numbers: ").split(' ')))
def remove_duplicates(lst):
    x=[]
    for i in lst:
        if i not in x:
            x.append(i)
    return x
print(f"List after removing duplicates: {remove_duplicates(lst)}")
