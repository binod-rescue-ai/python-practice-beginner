Score = float(input("Enter Score(0.0-1):"))
if Score < 0.0 or Score > 1.0:
    print("an error")
elif Score >= 0.9:
    Grade = "A"
elif Score >= 0.8:
    Grade = "B"
elif score >= 0.7:
    Grade = "C"
elif Score >= 0.6:
    Grade = "D"
else:
    Grade = "F"
#only print if Grade is Score < 0.0 or Score > 1.0.
print("your Grade is",Grade)
        