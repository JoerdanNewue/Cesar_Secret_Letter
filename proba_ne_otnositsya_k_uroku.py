a = [0] * 4
for i in range(len(a)):
    i = str(i + 1)
    print("Введите элемент массива " + i, end = " ")
    i = int(i)
    i = i - 1
    a[i] = int(input())
print("")
for i in range(len(a)):
    a[i] = a[i] * 2
for i in range(len(a)):
    print(a[i], end = " ")