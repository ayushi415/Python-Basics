## Compound Interest Calculator


principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

total_amount = principal * (1 + rate/100) ** time
Compound_Interest = total_amount - principal

print(f"Compound Interest: {Compound_Interest:.2f}");
print(f"Total Amount: {total_amount:.2f}");