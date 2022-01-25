s = input("Enter a string: ")
l = []

for i in range(0, len(s), 3):
    l.append([c for c in s[i : i + 3]])

print(l)
