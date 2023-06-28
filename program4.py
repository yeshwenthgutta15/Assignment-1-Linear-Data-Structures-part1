#   Write a program to print the first non-repeated character from a string

from collections import Counter

def first_non_repeated_character(string):
    counts = Counter(string)
    
    for char in string:
        if counts[char] == 1:
            return char
    
    return None
input_string = "yeshwenth"
result = first_non_repeated_character(input_string)
print(result)
