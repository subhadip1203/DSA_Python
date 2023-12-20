def find_element_to_remove(arr):
    total_sum = sum(arr)
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        remaining_sum = total_sum - current_sum
        if remaining_sum == current_sum:
            return arr[i]
    return -1

# Example usage
arr = [3, 1, 2, 4, 5]
element_to_remove = find_element_to_remove(arr)
print("Element to remove:", element_to_remove)
