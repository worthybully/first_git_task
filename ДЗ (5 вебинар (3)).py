str1 = input()
str2 = input()
str1.replace(' ', '')
str2.replace(' ', '')
set1 = set(str1)
set2 = set(str2)
if set1.intersection(set2) == set1:
    print('Это анаграмма')
else:
    print('Это не анаграмма')