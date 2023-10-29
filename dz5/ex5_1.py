def binnary_search(num, lst):
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
        mid = lst.index(num)
    return mid

if __name__ == '__main__':
    print(binnary_search(1, [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]))