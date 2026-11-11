#Get the second largest number. Hint: track two running values: largest and second_largest.
#SET largest = smaller than any possible value, or the first two items
#FOR each number in the list:
 #IF number > largest THEN
 #second_largest = largest
 #largest = number
 #ELSE IF number > second_largest AND number != largest THEN
 #second_largest = number

numbers = [12, 45, 7, 23, 56, 89, 34, 45, 18, 90]
largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n
second_largest = numbers[0]
#assume the 2nd number is the second largest one, then go through the list to find the actual second largest number that less than the largest number

for n in numbers:
    if n < largest and n > second_largest:
        second_largest = n


print("Second largest number:", second_largest)