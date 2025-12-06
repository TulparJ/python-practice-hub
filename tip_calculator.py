# Bill + Tip + Split Calculator

bill = float(input("Total bill amount: $"))
tip_percent = float(input("Tip percentage (e.g., 10, 15, 20): "))
people = int(input("Number of people splitting: "))

tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount
split_amount = total_bill / people

print(f"\nTip amount: ${tip_amount:.2f}")
print(f"Total with tip: ${total_bill:.2f}")
print(f"Each person pays: ${split_amount:.2f}")
