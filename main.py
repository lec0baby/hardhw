from dz3.ex3_1 import frik

def search(lst: list, num: int):
    low = 0 
    high = len(lst) - 1
    mid = len(lst) // 2
    
    while lst[mid] != num and low <= high:
        if lst[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
           
    if low > high:
        return None
    elif lst.count(num) > 1:
        mid = mid - (lst.count(num) // 2)
        return mid
    return mid

lst = frik(int(input()))
num = int(input())
#lst = [1, 2, 2, 3, 4]
#num = 2
print(search(lst, num))
