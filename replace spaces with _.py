str=input("Enter a string: ")

def replace_string_with_underscore(str):
    return str.replace(" ", "_")
print(f"String after replacing space with underscore: {replace_string_with_underscore(str)}")