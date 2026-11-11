#Write the program to ask user to enter a positive integer and then display its divisors

n = int(input("Enter a positive number: "))

if n <= 0:
    print("Error: Please enter a positive number.")

else:
    for i in range(1, n + 1):
        if (n % i == 0):
          print(i, end=" ")
