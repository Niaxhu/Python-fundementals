# Q - print all multiples of 5 between 1 and 100 (including both 1 and 100). Use WHILE and FOR

# method 1
# for i in range(5,100 + 1, 5):
    # print(i)

# method 2
#if i % 5 == 0: checks whether a number is divisible by 5 without a remainder.
for i in range(1,100 + 1):
    if i % 5 == 0:
        print(i)