#Calculate and display the result of 1 + 1/2 + 1/3 + 1/4 + … + 1/N for any given positive N.
# teaching me - how to use a loop to calculate a running total, where each term involves division.

n = int(input("Enter number: ")) # Asks the user to enter a number and converts it into an integer.

if n <= 0:
    print("Error: Please enter a positive number.")

s = 0 #Creates a variable called s to store the running total. It starts at zero.
for i in range(1, n + 1): #Loops from 1 up to N, including N.
    s = s + 1/i #Calculates each fraction and adds it to the running total.

print ("Result: ", s) #Displays the final total after the loop finishes.

