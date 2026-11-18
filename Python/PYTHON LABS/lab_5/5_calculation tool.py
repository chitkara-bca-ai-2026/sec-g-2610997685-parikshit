import math

print("=" * 40)
print("         MATH OPERATIONS HELPER")
print("=" * 40)

# Accept base number
base_number = float(input("Enter a base number: "))

# Accept power
power_input = float(input("Enter a power: "))

# Accept fractional measurement
fraction_value = float(input("Enter a fractional measurement: "))

# Perform calculations
raised_value = math.pow(base_number, power_input)
root_value = math.sqrt(base_number)
rounded_up = math.ceil(fraction_value)
rounded_down = math.floor(fraction_value)

# Display results
print("\n--- Output ---")
print(f"Base Number           : {base_number}")
print(f"Power                 : {power_input}")
print(f"Raised Value (pow)    : {raised_value}")
print(f"Square Root (sqrt)    : {root_value:.2f}")
print(f"Fractional Value      : {fraction_value}")
print(f"Rounded Up (ceil)     : {rounded_up}")
print(f"Rounded Down (floor)  : {rounded_down}")

print("=" * 40)