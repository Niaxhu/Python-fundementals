num = int(input("Enter number: "))

if 1 <= num <= 100:
    print("num is between 1 and 100 inclusive.")

    if num % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
else:
    print("num is NOT between 1 and 100 inclusive.")