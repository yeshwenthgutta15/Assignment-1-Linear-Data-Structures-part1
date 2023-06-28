#   Write a program to check if two strings are a rotation of each other

def rotations(string1, string2):
    if len(string1) != len(string2):
        return False
    
    concatenated_strings = string1 + string1
    
    if string2 in concatenated_strings:
        return True
    
    return False

# Example usage
str1 = "yeshwenth"
str2 = "htnewhsey"
result = rotations(str1, str2)
print(result)
