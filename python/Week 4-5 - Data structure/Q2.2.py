#Q-Find largest number without using max(). Expected: 90. Hint: initialise your "largest so far" using the first item of the list, not zero (why not zero? think about a list of all-negative numbers).

numbers = [12, 45, 7, 23, 56, 89, 34, 45, 18, 90]

#method 1
largest = numbers[0] #assume the 1st number is the largest one, then go through the list to find the actual largest number

for n in numbers:
   if n > largest:
       largest = n
print("Largest number:", largest)

#method 2
#sort the list and get the 1st number as the largest number
sortedNumbers = sorted(numbers, reverse = True) #sort
largest = sortedNumbers[0]
print("Largest number:", largest)