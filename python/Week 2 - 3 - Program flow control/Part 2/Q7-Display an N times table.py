#Write a program to display a N times table. N is a positive integer number

n = int(input("Enter number: ")) #Asks the user to enter a number and converts it into an integer.

if n <= 0:
    print("Error: Please enter a positive number.")
else:
  for i in range(1, 11): #Loops from 1 to 10. Remember, range() excludes 11
      print (i, " x ", n, " = ", i * n) #Displays the multiplication sum and calculates the answer using i * n
