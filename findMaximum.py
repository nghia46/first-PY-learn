# Find largest number of array using bubble_sort
def finMaxArr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap elements
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr[n-1]

numbers = [64, 34, 25, 12, 22, 111, 90]
result = finMaxArr(numbers)
print(result)