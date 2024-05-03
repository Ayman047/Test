def subarray_sum(arr, target_sum):
    current_sum = arr[0]
    start = 0

    for end in range(1, len(arr)):
        # Remove elements from the start of the window until the current sum is less than or equal to the target sum
        while current_sum > target_sum and start < end:
            current_sum -= arr[start]
            start += 1

        # If current sum equals target sum, return the indices of the subarray
        if current_sum == target_sum:
            return start, end - 1

        # Add the current element to the sum
        current_sum += arr[end]

    # Check if the last subarray forms the target sum
    if current_sum == target_sum:
        return start, len(arr) - 1

    # If no subarray is found, return None
    return None

# Example usage
arr = [1, 4, 20, 3, 10, 5]
target_sum = 33
result = subarray_sum(arr, target_sum)
if result:
    start, end = result
    print("Subarray found from index", start, "to", end, ":", arr[start:end + 1])
else:
    print("No subarray found with the given sum")
