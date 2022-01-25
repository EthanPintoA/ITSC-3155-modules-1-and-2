gradeNum = float(input("Enter a grade from 0 to 100: "))
gradeLetter = ""

if gradeNum >= 90:
    gradeLetter = "A"
elif gradeNum >= 80:
    gradeLetter = "B"
elif gradeNum >= 70:
    gradeLetter = "C"
elif gradeNum >= 60:
    gradeLetter = "D"
else:
    gradeLetter = "F"

print(f"Your grade is {gradeLetter}")
