l1 = []
l2 = []

for _ in range(5):
    i = int(input("Enter a number for the first list: "))
    l1.append(i)

for _ in range(5):
    i = int(input("Enter a number for the second list: "))
    l2.append(i)

print(list({n for n in l1 if n in l2}))
