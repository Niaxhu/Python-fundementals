#Write python codes for following flowcharts
#Find GCD by iterative divisor reduction

x = int(input("Enter number: ")) #Asks the user for the first integer.
y = int(input("Enter number: ")) #Asks the user for the second integer.

divisor = x ##Starts by assuming the first number is the possible greatest divisor.

while y % divisor != 0: #Checks whether the divisor divides y exactly. Continues while there is a remainder.
    divisor = divisor - 1 #Reduces the potential divisor by one.
    while x % divisor != 0: #Checks whether the current divisor divides x exactly.
        divisor = divisor - 1 #Keeps reducing the divisor until it divides x exactly.
print("Divisor: ", divisor) #Displays the resulting divisor.


#GCD stands for Greatest Common Divisor - It means finding the largest whole number that divides two numbers exactly, without leaving a remainder
#teaches me:
#How to use a while loop, nested while loops, modulo to test divisibility, repeatedly update a variable, solve a mathematical problem using an algorithm
#
#