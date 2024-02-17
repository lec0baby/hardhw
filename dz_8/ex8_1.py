def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
<<<<<<< HEAD
    pivot = arr[0]
    small = [x for x in arr[1:] if x <= pivot]
    big = [x for x in arr[1:] if x > pivot]
    return quick_sort(small) + [pivot] + quick_sort(big)
=======
        pivot = arr[0]
        small = [x for x in arr[1:] if x <= pivot]
        big = [x for x in arr[1:] if x > pivot]
        return quick_sort(small) + [pivot] + quick_sort(big)
>>>>>>> ba3d9abe8962529bd62aac1942ddf7e28cdcf20a
    

def stalin_sort(arr):
    if len(arr) <= 1:
        return arr
<<<<<<< HEAD
    else:
        
=======
    same = []
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            same.append(arr[i])
    return [j for j in arr if j not in same]
>>>>>>> ba3d9abe8962529bd62aac1942ddf7e28cdcf20a
