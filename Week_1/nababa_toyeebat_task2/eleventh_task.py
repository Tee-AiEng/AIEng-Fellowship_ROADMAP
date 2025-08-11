Amount_in_naira = float(input("Amount in Naira(#): "))
exg_rte_to_dollars = float(input("Exchange rate to USD($): "))
exg_rte_to_pounds = float(input("Exchange rate to GBP(£): "))
conversion_to_USD = Amount_in_naira /exg_rte_to_dollars
conversion_to_GBP = Amount_in_naira /exg_rte_to_pounds
print(f"Amount in naira\tExchange rate to USD\tEchange rate to GBP\n{Amount_in_naira}\t\t{exg_rte_to_dollars}\t\t{exg_rte_to_pounds}\nConverted to USD: ${conversion_to_USD:,.2f}\nConverted to GBP: £{conversion_to_GBP:,.2f}")