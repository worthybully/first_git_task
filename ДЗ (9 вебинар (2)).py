num = int(input())
list1 = []
for i in range(2, num + 1):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1
            break
    if count == 0:
        list1.append(i)
print(list1)