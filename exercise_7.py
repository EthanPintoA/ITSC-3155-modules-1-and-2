l = []

while True:
    i = input("Enter a number or QUIT to quit: ")

    if i != "QUIT":
        l.append(int(i))
    else:
        break

print([n for n in l if n % 2 == 0])
