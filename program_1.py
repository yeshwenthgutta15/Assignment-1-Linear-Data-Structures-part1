#   Write a program to find all pairs of an integer array whose sum is equal to a given number?

def pairs_mine(arr, target_sum):
    pair = []
    seen = set()
    
    for num in arr:
        complementing = target_sum - num
        if complementing in seen:
            pair.append((num, complementing))
        seen.add(num)
    
    return pair
array = [2, 4, 6, 8, 6, -6, 4, 10, 8, 9]
target = 6
result = pairs_mine(array, target)
print(result)