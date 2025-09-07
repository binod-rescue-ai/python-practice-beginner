hours = float(input("Enter hours worked"))
rate = float(input("Enter rate per hour"))
if hours <= 40:
    pay = hours * rate
else:
    pay = 40 *rate + (hours - 40) *rate * 1.5
print("Total pay is:", pay)
