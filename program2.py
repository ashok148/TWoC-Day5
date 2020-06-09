l = list(map(int, input("Enter numbers: ").split(" ")))
for i in range(0, len(l) - 1):
    max1 = l[i + 1]
    for j in range(i + 2, len(l)):
        if (l[j] > max1):
            index = j
            max1 = l[j]
    l[i] = l[index]

print(l)