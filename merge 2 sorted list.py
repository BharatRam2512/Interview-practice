lst1=list(map(int, input("enter numbers for first list: ").split(" ")))
lst2=list(map(int, input("enter numbers for second list: ").split(" ")))
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1+lst2)
print(f"Merged sorted list: {merge_sorted_lists(lst1, lst2)}")