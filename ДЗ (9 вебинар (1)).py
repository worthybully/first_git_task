a = int(input())
b = int(input())
minimum = min(a, b)
maximum = max(a, b)
nok = None
number = maximum
while nok is None:
    if number % minimum == 0 and number % maximum == 0:
        nok = number
    else:
        number += maximum
print(nok)