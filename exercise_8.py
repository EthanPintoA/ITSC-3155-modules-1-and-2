l1 = []

for _ in range(10):
    n = int(input("Enter a number: "))
    l1.append(n)

print([i for i in l1 if l1.count(i) == 1])
