attempts = 0
correct_password = "python123"

while attempts < 1:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break
    attempts = attempts + 1
else:
    print("Access denied")