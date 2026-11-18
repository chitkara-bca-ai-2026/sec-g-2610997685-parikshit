course_fee = float(input("Enter Course Fee: "))
laboratory_charge = float(input("Enter Laboratory Charge: "))
library_charge = float(input("Enter Library Charge: "))
examination_charge = float(input("Enter Examination Charge: "))
concession = float(input("Enter Concession Amount: "))

# Calculations
gross_amount = course_fee + laboratory_charge + library_charge + examination_charge
net_amount = gross_amount - concession
yearly_amount = net_amount * 2
monthly_payment = yearly_amount / 12

# Display results
print()
print("Course Fee:", course_fee)
print("Laboratory Charge:", laboratory_charge)
print("Library Charge:", library_charge)
print("Examination Charge:", examination_charge)
print("Gross Amount:", gross_amount)
print("Concession:", concession)
print("Net Amount (After Concession):", net_amount)
print("Yearly Amount:", yearly_amount)
print("Monthly Payment:", round(monthly_payment, 2))