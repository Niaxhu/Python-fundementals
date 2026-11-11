room_rate = float(input("Enter room rate: "))
nights = int(input("Enter number of night: "))
service_cost = float(input("Enter service cost: "))

subtotal = (room_rate * nights) + service_cost
vat = subtotal * 0.20
total_bill = subtotal + vat

print("subtotal: ", subtotal)
print("vat: ", vat)
print("total bill: ", total_bill)