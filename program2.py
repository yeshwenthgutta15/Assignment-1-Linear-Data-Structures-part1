# Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reverseing_array(arr):
    start_point = 0
    ending = len(arr) - 1
    
    while start_point < ending:
        arr[start_point], arr[ending] = arr[ending], arr[start_point]
        start_point += 1
        ending -= 1
array = [1, 2, 3, 4, 5,6]
reverseing_array(array)
print(array)