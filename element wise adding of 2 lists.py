lst1=list(map(int,input("Enter number for first list:").split(" ")))
lst2=list(map(int,input("enter numbers for second list: ").split(" ")))

def add_list_elements(lst1, lst2):
    result=[]
    for i in range(len(lst1)):
        result.append(lst1[i]+lst2[i])
    return result

print(f" Element wise adding of two lists are: {add_list_elements(lst1,lst2)}")