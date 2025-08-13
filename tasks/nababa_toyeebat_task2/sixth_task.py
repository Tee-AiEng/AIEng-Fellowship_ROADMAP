cust_Full_name = input("Enter your Full name: ")
unit_consumed = int(input("Enter unit consumed(kWh): "))
cost_per_unit = float(input("Enter cost per unit(#): "))
total_bill = unit_consumed * cost_per_unit
print(f"Customer’s full name\tUnits consumed (kWh)\tCost per unit(#)\n{cust_Full_name}\t\t\t{unit_consumed}\t\t\t{cost_per_unit}\n\n\nTotal bill =\t\t#{total_bill}")
