lst=list(map(int, input("enter numbers for the list: ").split(" ")))
def sum_and_svg(lst):
    sum=0
    for i in lst:
        sum+=i
        
    avg=sum/len(lst)
    return sum, avg
total, avg = sum_and_svg(lst)   
print(f"Sum of the list is: {total}")
print(f"Average of the list is: {int(avg)}")