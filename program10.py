#   Write a program to find the smallest number using a stack.

def find_smallest_number(stack):
    if len(stack) == 0:
        return None
    
    smallest = stack.pop()
    
    if len(stack) > 0:
        temp = find_smallest_number(stack)
        if temp < smallest:
            smallest = temp
    
    return smallest

stack = [5, 3, 8, 1, 2, 10]
small_number = find_smallest_number(stack)
print(small_number)
