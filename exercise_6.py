rowIn = int(input("Enter a row num from 1 to 5: "))
colIn = int(input("Enter a col num from 1 to 5: "))

l = [["0" for _ in range(5)] for _ in range(5)]
l[rowIn - 1][colIn - 1] = "1"

for row in l:
    print(" ".join(row))
