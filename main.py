def stalin_sort(arr):
    return [arr[i] for i in range(len(arr) - 1, 0, - 1) if arr[i] >= arr[i - 1]]

print(stalin_sort([3, 2, 1, 0]))