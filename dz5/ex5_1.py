def binnary_search(num, lst):
    while lst.count(num) >  1:
        lst.remove(num)
    
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
    else:
        return mid
    
if __name__ == '__main__':
    print(binnary_search(7, [7, 7, 7, 7]))