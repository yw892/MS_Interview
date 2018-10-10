def binary_search_next_larger_pos(arr, val, low, high):
    """
    The function is to find the position of the minimum number that is larger than 
    val in a descending order list by using the binary search
    :param arr: list
    :val: integer
    :low: integer
    :high: integer
    :return: integer, if val is larger than the largest value in the list, return -1
    """    
    if arr[-1] > val:
        return len(arr) - 1
    elif arr[0] < val:
        return -1
    while low <= high:
        mid = int((low + high) / 2)
        print(mid)
        if arr[mid] < val:
            high = mid - 1
        elif arr[mid] > val:
            low = mid + 1
        else:
            return mid
    return high
    
def next_number(num):
    """
    The function is to find the minimum number which is larger than given number
    :param num: integer
    :return: integer, if num is already the maximum number, return None
    """
    num_list = list(map(int, str(num)))
    if len(num_list) <= 1:
        return num
    pos = len(num_list) - 2
    while pos >= 0:
        if num_list[pos] < num_list[pos+1]:
            break
        pos -= 1
    if pos < 0:
        print('No next number, maximum number already')
        return
    else:
        path = num_list[pos+1:]
        print(path)
        replace_pos = binary_search_next_larger_pos(path, num_list[pos], 0, len(path))
        print(replace_pos)
        print(num_list[pos], path[replace_pos])
        path[replace_pos], num_list[pos] = num_list[pos], path[replace_pos]
        return int(''.join(list(map(lambda x:str(x), num_list[:pos+1] + path[::-1]))))

print(next_number(987136524))
