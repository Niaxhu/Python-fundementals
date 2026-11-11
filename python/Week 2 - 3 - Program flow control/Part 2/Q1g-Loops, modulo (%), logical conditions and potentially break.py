number = 1

while True:
    if number % 7 == 0 and number % 3 == 0:
        print("Found:", number)
        break
    number = number + 1