#Enter a positive number N and display output below. For example, N = 5

n = int(input("Enter number: ")) #Asks the user for a number and converts it into an integer.

for i in range(1, n + 1): #Outer loop. Controls how many rows are printed.
    for j in range(1, i + 1): #Inner loop. Controls which numbers appear on each row.
        print(j, end=' ') #Prints the current value of j on the same line, followed by a space.
    print() #Moves to a new line after the inner loop finishes.

print() #blank lines
print() #blank lines
####
for i in range(0, n ): #Outer loop. Runs from 0 to n-1, controlling the rows.
    for j in range(1, n - i + 1): #Inner loop. Controls how many numbers are printed on each row.
        print(j, end=' ') #Prints each number on the same line, separated by a space
    print() #Moves to the next line when the inner loop finishes.