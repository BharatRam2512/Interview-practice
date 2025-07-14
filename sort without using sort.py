def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot =arr[0]
        greater=[x for x in arr[1:] if x>pivot]
        lesser=[x for x in arr[1:] if x<=pivot]
    return quick_sort(lesser)+[pivot]+quick_sort(greater)

arr=[1,23,54,26,12,84,22,4,6,33]
print(quick_sort(arr))