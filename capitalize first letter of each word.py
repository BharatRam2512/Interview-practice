str=input("enter a string: ")
def capitalize_first_letter_of_each_word(str):
    return ' '.join(word.capitalize() for word in str.split())
print(f"String after capitalizing first letter of each word: {capitalize_first_letter_of_each_word(str)}")