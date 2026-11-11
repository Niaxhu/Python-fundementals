import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

C = a + b + c
p = C / 2

S = math.sqrt(p * (p-a) * (p-b) * (p-c))

print("Perimeter:", C)
print("Semi-perimeter:", p)
print("Area:", S)