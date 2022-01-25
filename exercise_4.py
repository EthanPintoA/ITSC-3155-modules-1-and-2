l = []
n = int(input("Enter a number: "))

for i in range(n):
    n2 = float(input(f"Enter number {i + 1}: "))
    l.append(n2)

print(f"List: {l}")
print(f"Average: {sum(l) / len(l)}")
