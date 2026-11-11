
years = int(input("Enter the year: "))
if (years % 400 == 0 and years %100 == 0) or (years % 4 == 0 and years % 100 != 0):
    print ( years, "is a leap year")
else:
    print ( years, "is not a leap year")
