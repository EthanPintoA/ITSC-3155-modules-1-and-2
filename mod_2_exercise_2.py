s = input("Enter a string: ")

lower = [c for c in s if c.islower()]
not_lower_or_space = [c for c in s if not c.islower() and c != " "]

print("".join(lower + not_lower_or_space))
