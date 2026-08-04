##  Simple Interest Calculator.

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print(f"Simple Interest: {simple_interest:.2f}")
print(f"Total Amount: {total_amount:.2f}")