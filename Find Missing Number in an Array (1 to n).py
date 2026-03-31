# Find missing number in an array (1 to n)

def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    array_sum = 0

    for num in arr:
        array_sum += num

    return total_sum - array_sum


# Input
array = [1, 2, 3, 5, 6]   # Missing number is 4
n = 6

# Function call
result = find_missing_number(array, n)

# Output
print("Missing number is:", result)
