#   Write a program to check if all the brackets are closed in a given code snippet.

def reverse_stack(stack):
    if len(stack) <= 1:
        return stack
    
    last_element = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, last_element)

def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
        return
    
    last_element = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(last_element)

stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)