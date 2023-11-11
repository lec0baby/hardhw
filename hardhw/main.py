def binnary_search(num: int, lst: list):
    low, high = 0, len(lst)
    while low < high:
        mid = (low + high) // 2
        if lst[mid] < num:
            low = mid + 1
        else:
            high = mid
        return low if low < len(lst) and lst[low] == num else None
    
if __name__ == '__main__':
    print(binnary_search(1, [1, 1, 1, 1, 1]))