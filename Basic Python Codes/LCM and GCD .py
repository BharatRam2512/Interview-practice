def gcd(a,b):
    while b!=0:
        a,b=b, a%b
    return a


#method 2

def gcd(a,b):
    if b==0:
        return a
    return gcd(a,b%a)

#method 3
def gcd(a,b):
    i=1 
    while (i<=a and i<=b):
        if a%i==0 and b%i==0:
            gcd=i
        i+=1
    return gcd


a=int(input("enter number a: "))
b=int(input("enter number b: "))
print(f"GCD of {a},{b} is {gcd(a,b)}")

lcm=(a*b)//gcd(a,b)
print(f"LCM of {a},{b} is {lcm}")   