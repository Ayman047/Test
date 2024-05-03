def chocolate(arr, n, m):
    if n==0 or m==0:
        return 0
    if n<m:
        return-1
    
    arr.sort()
    min_diff = float('inf')
    for i in range(n-m+1):
        diff = arr[n-m+1] + arr[i]
        min_diff = min(min_diff, diff )
        
    return min_diff
        
arr = [7, 3, 2, 4, 9, 12, 56]
n = len(arr)  # Number of students
m = 3         # Number of chocolates
result = chocolate(arr, n, m)
print("Minimum difference:", result)
        