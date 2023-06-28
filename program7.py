#   Write a program to convert prefix expression to infix expression.

def operator_is(char):
    operators = {'+', '-', '*', '/'}
    return char in operators

def prefixing_to_infixing(expression):
    stack = []
    
    for char in reversed(expression):
        if operator_is(char):
            operand1 = stack.pop()
            operand2 = stack.pop()
            infixing_expression = f"({operand1}{char}{operand2})"
            stack.append(infixing_expression)
        else:
            stack.append(char)
    
    return stack.pop()

prefixing_expression = "-+AB-CDE"
infixing_expression = prefixing_to_infixing(prefixing_expression)
print(infixing_expression)