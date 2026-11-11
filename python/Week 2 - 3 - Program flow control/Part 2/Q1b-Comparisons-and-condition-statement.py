a = float(input("Enter a value for a = "))
b = float(input("Enter a value for b = "))
c = float(input("Enter a value for c = "))

x1 = ((-b) + (b*b - 4*a*c)**0.5) / (2*a)
x2 = ((-b) - (b*b - 4*a*c)**0.5) / (2*a)

print("The results are", x1, x2)