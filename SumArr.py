def SumArr(arr):
    total = 0
    for num in arr:
        total += num
    return total

numbers = [1, 2, 3]
sum = SumArr(numbers)
print(sum/len(numbers))