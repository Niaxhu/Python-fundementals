#Count uppercase/lowercase characters
lower_case = 0 #Creates a counter for lowercase letters.
upper_case = 0 #Creates a counter for uppercase letters.

while True: #Starts a loop that continues indefinitely until told to stop.
    user_input = input("Enter a character or press enter to stop:") #Asks the user to enter a character.
    if 'a' <= user_input <= 'z':  # if character in range('a', 'z'): #Checks whether the input is between lowercase a and z.
        lower_case = lower_case + 1 #Increases the lowercase counter by one.
    elif 'A' <= user_input <= 'Z': #Checks whether the input is between uppercase A and Z.
        upper_case = upper_case + 1 #Increases the uppercase counter by one.
    elif user_input == "": #Checks whether the user pressed Enter without typing anything.
        print("Enter key pressed!") #
        break 	#Stops the loop.

print("totals lower case", lower_case) #Displays the final totals after the loop ends.
print("totals upper case", upper_case) #Displays the final totals after the loop ends.

#method 2
lower_case = 0
upper_case = 0

ch = input("Enter character: ") #Gets the first character before the loop starts.

while ch != "": #in python, if only press Enter key, the input only contains empty string #Continues looping while the input isn't empty.
    if 'a' <= ch <= 'z':  # if character in range('a', 'z'): #Checks for a lowercase character.
        lower_case = lower_case + 1
    elif 'A' <= ch <= 'Z': # Checks for a lowercase character.
        upper_case = upper_case + 1
    ch = input("Enter character: ") #Asks for the next character so the loop can continue

print("totals lower case", lower_case) #Displays the totals once the user presses Enter.
print("totals upper case", upper_case)


#t introduces a new concept: checking whether a character falls within a range of letters
#Character exercise teaching me:
# while loops - Repeat instructions while a condition is satisfied.
# != - Check whether two values are different.
# Counters - Keep track of how many times something occurs.
# break - Exit a loop immediately.
# String comparisons - Check whether characters fall within a particular range.
# Input validation/control - Control how the program responds to user input.

# GCD exercise teaching me
# Nested loops - Put one loop inside another.
# % modulo - Check whether numbers divide exactly.
# in GCD also - while loop, !=, input validation/ control
