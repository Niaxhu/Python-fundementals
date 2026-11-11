hourly_rate =float(input("Enter hourly rate: "))
hours_worked =int(input("Enter hours worked: "))

if  hours_worked <= 40:
    pays = hourly_rate * hours_worked
else:
    pays = 40 * hourly_rate + (hours_worked - 40) * hourly_rate * 1.5

print("Your salary is ", pays)
