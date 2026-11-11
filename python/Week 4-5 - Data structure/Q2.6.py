#Q-Remove elements if multiplication of 3
numbers = [3, 5, 9, 10, 5, 2, 3, 6, 2, 6]

selected_numbers = []
for n in numbers:
    if n % 3 != 0:
        selected_numbers.append(n)

print(selected_numbers)

#method 2
selected_numbers = [number for number in numbers if number % 3 != 0]
print(selected_numbers)
