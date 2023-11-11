n = int(input())
towns = set()
count_towns = 0
for i in range(n):
    towns.add(input())
for i in towns:
    if i in towns:
        count_towns += 1
print(count_towns)