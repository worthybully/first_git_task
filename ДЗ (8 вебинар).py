def find_max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        maximum = find_max_recursive(lst[1:])
        return lst[0] if lst[0] > maximum else maximum