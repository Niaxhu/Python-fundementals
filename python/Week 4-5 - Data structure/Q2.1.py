#Build small, related operations on the same list, one at a time. This task explicitly practise counter,accumulator, and comparison patterns applied to lists. Given a list of integers
#Q - Find all even numbers. Example expected: [12, 56, 34, 18, 90]
numbers = [12, 45, 7, 23, 56, 89, 34, 45, 18, 90]
evenNumbers = []

#method1
for n in numbers:
    if n % 2 == 0:
        evenNumbers.append(n)

print("Even numbers:", evenNumbers)

#method2
evenNumbers = [n for n in numbers if n % 2 == 0]

print("Even numbers:", evenNumbers)