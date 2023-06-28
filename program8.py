#   Write a program to check if all the brackets are closed in a given code snippet.

def are_brackets_balanced(code):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    
    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False
    
    return len(stack) == 0

code_snippet = "(a + b) * [c - {d / e}]"
result = are_brackets_balanced(code_snippet)
print(result)