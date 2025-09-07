hours = float(input('total hours worked:'))
normal_rate = 10.50
if hours <= 40:
    pay = hours * normal_rate
else:
    normal_pay = 40 * normal_rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * normal_rate * 1.5
    total_pay = normal_pay + overtime_pay
print('gross pay is', total_pay)