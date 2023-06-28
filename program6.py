#   Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def operator_is(char):
    operators = {'+', '-', '*', '/'}
    return char in operators

def postfixing_to_prefixing(expression):
    stack = []
    
    for char in expression:
        if operator_is(char):
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix_expression = char + operand1 + operand2
            stack.append(prefix_expression)
        else:
            stack.append(char)
    
    return stack.pop()
postfix_expression = "AB+CD-/"
prefix_expression = postfixing_to_prefixing(postfix_expression)
print(prefix_expression)