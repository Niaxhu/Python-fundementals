num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
print((num1+num2)/2)

if num1 > num2:
    print("the largest number is:", num1)
elif(num1 > num2):
    print("the smallest number is:", num2)
else:
    print("both numbers are equal")