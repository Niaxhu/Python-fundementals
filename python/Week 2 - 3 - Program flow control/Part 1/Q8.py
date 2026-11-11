# Input Parameters
distance = float(input("Enter the distance between cities (in mile): "))

driver_status = int (input ("What is the driver status? (1: Junior, 2: Senior): "))

if driver_status == 1:
    hourly_rate = 15
else:
    hourly_rate = 40

fuel_status = int (input ("What is the type of fuel? (1: petrol, 2: diesel): "))

if fuel_status == 1:
    fuel_cost_per_unit = 5
    fuel_consumption_rate = 1/15
else:
    fuel_cost_per_unit = 6
    fuel_consumption_rate = 1/25

road_type = int (input ("What is the type of road? (1: A-road, 2: motorway): "))
if fuel_status == 1:
    cruise_speed = 60
else:
    cruise_speed = 70

min_passengers = float(input("Enter the minimal number of passengers expected: "))
max_ticket_price = float(input("Enter the highest affordable ticket price per passenger (£): "))

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