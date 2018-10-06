def next_number(num):
    """
    The function is to find the minimum number which is larger than given number
    :param num: integer
    :return: integer, if num is already the maximum number, return None
    """
    num_list = list(map(int, str(num)))
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
        replace_pos = 0
        for i in range(1, len(path)):
            if path[i] > num_list[pos] and path[i] < path[replace_pos]:
                replace_pos = i
        path[replace_pos], num_list[pos] = num_list[pos], path[replace_pos]
        return int(''.join(list(map(lambda x:str(x), num_list[:pos+1] + path[::-1]))))

print(next_number(987136542))

from functools import reduce
def num_combinations(num_input):
    """
    The function is to compute the number of combinations of characters given an input number 
    :param num_input: integer
    :return: integer
    """
    return reduce(lambda x, y: x*y, list(map(lambda x:3 if x!=9 else 4, map(int, str(num_input)))))
print(num_combinations(56))
print(num_combinations(34569))

def all_combinations(input_num):
    """
    The function is to return all the combinations of characters given an input number 
    :param num_input: integer like 34569
    :return: list
    """
    dict_ = {1:[], 2:[['a'],['b'],['c']], 3:[['d'],['e'],['f']], 4:[['g'],['h'],['i']], 5:[['j'],['k'],['l']], 
         6:[['m'],['n'],['o']], 7:[['p'],['q'],['r'],['s']], 8:[['t'],['u'],['v']], 9:[['w'],['x'],['y'],['z']]}
    list_num = list(map(int, str(input_num)))
    return reduce(lambda exist,i: dict_[list_num[i]] if isinstance(exist, int) 
       else [x+y for x in exist for y in dict_[list_num[i]]], [0] + list(range(len(list_num))))

res = all_combinations(34567)
print(len(res))
print(res[:10])
