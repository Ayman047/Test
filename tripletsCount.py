def count_triplets(arr):
    cnt = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # If it satisfies the given conditions
                if arr[k] < arr[i] and arr[i] < arr[j]:
                    cnt += 1
    # Return the final count
    return cnt

# Example usage
arr = [1, 3, 2, 4, 5]
print("Count of triplets:", count_triplets(arr))  # Output: 1
