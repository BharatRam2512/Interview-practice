a=int(input("enter a number1: "))
b=int(input("enter a number2: "))
op=input("enter an operation you want to perform: ")
def calculator(a,b,op):
    if op=="+":return a+b
    elif op =="-": return a-b
    elif op == "*": return a*b
    elif op == "/": return a/b
    elif op =="//": return a//b
print(calculator(a,b,op))