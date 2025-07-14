n1=input("enter string1: ")
n2=input("enter string2: ")

def are_anagrams(n1,n2):
    return sorted(n1)==sorted(n2)

print(f"Are the given two strings anagrams? {are_anagrams(n1,n2)}")
