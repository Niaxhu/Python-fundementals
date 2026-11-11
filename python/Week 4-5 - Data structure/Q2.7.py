#Q-if element of list is between 30 and 45, make it 1 else 0
#method 1: use list comprehension

numbers = [3, 5, 9, 10, 5, 2, 3, 6, 2, 6]
flags = [1 if 30 <= number <= 45 else 0 for number in numbers]
print(flags)
#method 2: you can use a for loop to iterate through the list and replace values in range with 1, else 0
flags = []
for number in numbers:
    if 30 <= number <= 45:
        flags.append(1)
    else:
        flags.append(0)
print(flags)
