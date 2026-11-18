print("=" * 50)
print("          Data Type Conversion")
print("=" * 50)

item_name = input("Enter the item name: ")
unit_price = float(input("Enter the item price: "))
item_count = int(input("Enter the item quantity: "))

total_cost = unit_price * item_count


print("-" * 50)
print("        Type Conversion Summary")
print("-" * 50)
print("variable       value    python type")
print("-" * 50)
print(f"item name      {item_name}   {type(item_name)}")