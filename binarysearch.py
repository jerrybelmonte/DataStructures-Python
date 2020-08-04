# Binary search function using iterative approach
def binary_search(input_array, value):
    left = 0
    right = len(input_array) - 1
    key = -1
    while left <= right:
        mid = (left + right)//2
        if value > input_array[mid]:
            left = mid + 1
        elif value < input_array[mid]:
            right = mid - 1
        else:
            key = mid
            break
    return key


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
