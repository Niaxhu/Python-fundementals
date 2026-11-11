#to find numbers that only appear once in the list, you can count how many times each number exists in the list
#then find numbers which appear once

numbers = [3, 5, 9, 10, 5, 2, 3, 6, 2, 6]
# method 1
frequency = []

for i in range(len(numbers)):
    count = 1
    for j in range(len(numbers)):
        if numbers[i] == numbers[j] and i != j:
            count = count + 1
    frequency.append(count)

  #after counting, display unique values
selected_numbers = []
for i in range(len(numbers)):
    if frequency[i] == 1: # only appear once
        selected_numbers.append(numbers[i])

print(selected_numbers)

#method 2: use built-in function count() of list which counts how many times one item appears in list
selected_numbers = []

for n in numbers:
    if numbers.count(n) == 1:
        selected_numbers.append(n)

print(selected_numbers)