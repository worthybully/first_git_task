def maximum(*num):
    max_number = 0
    for i in num:
        if i > max_number:
            max_number = i
    return max_number