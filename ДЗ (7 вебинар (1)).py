list1 = [1, 2, 3, 4, 5]
list2 = [8, 14, 5, 12, 10, 6, 4, 1, 18]
sum_of_lists = list(map(lambda x, y: x + y, list1, list2)) + list1[len(list2):] + list2[len(list1):]
print(sum_of_lists)