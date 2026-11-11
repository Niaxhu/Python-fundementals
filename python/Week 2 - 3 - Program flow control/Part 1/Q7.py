# Input Parameters
distance = float(input("Enter the distance between cities (in mile): "))
hourly_rate = float(input("Enter the driver's hourly rate (£/hour): "))
fuel_cost_per_unit = float(input("Enter the cost of fuel per unit (£/unit): "))
fuel_consumption_rate = float(input("Enter the fuel consumption rate (gallon/mile): "))
cruise_speed = float(input("Enter the cruise speed of the coach (mile/h): "))
min_passengers = int(input("Enter the minimum expected number of passengers: "))
max_ticket_price = float(input("Enter the maximum ticket price per passenger (£): "))


# Calculations
travel_time = distance / cruise_speed  # in hours
labour_cost = travel_time * hourly_rate
total_fuel_cost = distance * fuel_consumption_rate * fuel_cost_per_unit
total_cost = labour_cost + total_fuel_cost
overhead = total_cost * 0.20
total_required_income = total_cost + overhead
total_ticket_income = min_passengers * max_ticket_price

# Display Results
print("\n=== Calculation Results ===")
print(f"Travel Time: {travel_time:.2f} hours")
print(f"Labour Cost: £{labour_cost:.2f}")
print(f"Fuel Cost: £{total_fuel_cost:.2f}")
print(f"Total Cost: £{total_cost:.2f}")
print(f"Overhead (20%): £{overhead:.2f}")
print(f"Total Required Income (including overhead): £{total_required_income:.2f}")
print(f"Total Ticket Income: £{total_ticket_income:.2f}")

# Viability Assessment
if total_ticket_income >= total_required_income:
    print("\n*** Financial Viable ***")
else:
    print("\n*** Not Viable ***")