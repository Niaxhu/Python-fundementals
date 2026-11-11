# Q - o count all the even numbers up to a user defined stopping point.
# Stage 1: Read the stopping value from the user - Ask the user to enter a number
# Stage 2: Set a counter for even numbers to 0 - Create a variable to count the even numbers
# Stage 3: Loop from 1 up to the stopping value. - Check each number in the sequence
# Stage 4: For each number, decide whether it is even. - Use % 2 == 0 to check for even numbers
# Stage 5: If it is even, increase the counter. - Add 1 to the counter when an even number is found
# Stage 6: After the loop, display the counter. - Show the total number of even numbers


n = int(input("Enter number: "))

# method 1 - Using for and if (Checks every number to find even numbers_
for i in range(0, n):
    if i% 2 == 0:
        print(i)

# method 2 - Using increments of 2 (Jumps directly between even numbers)
print("Another")
for i in range(0, n, 2):
    print(i)

# method 3 - Using while and if (Checks every number (but needs an increment))
i = 0
while i < 10:
    if i % 2 == 0:
        print(i)

# method 4 - Using while with increments of 2 (Jumps directly between even numbers)
i = 0
while i < 10:
    print(i)
    i = i + 2