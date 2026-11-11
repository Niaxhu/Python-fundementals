#Q-Get unique values

numbers = [3, 5, 9, 10, 5, 2, 3, 6, 2, 6]

#get unique numbers

unique_numbers = []

for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)

print(unique_numbers)