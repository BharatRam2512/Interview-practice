n=input("enter a string: ")
vowel_count=0
consonant_count=0
digit_count=0
space_count=0

for char in n:
    if char.isdigit():
        digit_count+=1
    elif char==' ':
        space_count+=1
    elif char.lower() in 'aeiou':
        vowel_count+=1
    elif char.isalpha():
        consonant_count+=1

print(f"the no of vowels in the string is: {vowel_count}, the no of consonants in the string is: {consonant_count},\
the no of digits in the stirng is: {digit_count}, the no of spaces in the string is : {space_count}")
