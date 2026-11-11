
list_a = (1, 2, 3, 4, 5)
list_b = (4, 5, 6, 7, 8)

diff_nums = []

for n in list_a:
    if (n not in list_b) and (n not in diff_nums):
       diff_nums.append(n)

for n in list_b:
    if (n not in list_a) and (n not in diff_nums):
        diff_nums.append(n)

print(diff_nums)