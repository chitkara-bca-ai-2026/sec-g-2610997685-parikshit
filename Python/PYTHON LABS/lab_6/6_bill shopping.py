print("=" * 50)
print("       FASHION SHOP INVOICE SYSTEM")
print("=" * 50)

# Accept buyer details
buyer_name = input("Enter Buyer Name: ")
apparel_name = input("Enter Apparel Name: ")
unit_cost = float(input("Enter Cost of one apparel: "))
pieces = int(input("Enter Number of Pieces: "))

# Calculate payable amount
payable_amount = unit_cost * pieces

# Display invoice
print("\n" + "=" * 50)
print("                INVOICE")
print("=" * 50)

print(f"Buyer Name     : {buyer_name}")
print(f"Apparel Name   : {apparel_name}")
print(f"Cost per Piece : Rs. {unit_cost:.2f}")
print(f"Pieces         : {pieces}")
print(f"Payable Amount : Rs. {payable_amount:.2f}")

print("=" * 50)