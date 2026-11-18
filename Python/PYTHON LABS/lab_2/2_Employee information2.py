worker_name = input("Enter Worker Name: ")
print("Data type:", type(worker_name))

worker_code = int(input("Enter Worker Code: "))
print("Data type:", type(worker_code))

wage = float(input("Enter Wage: "))
print("Data type:", type(wage))

division = input("Enter Division: ")
print("Data type:", type(division))

availability_input = input("Is the worker currently employed? (yes/no): ")
is_employed = availability_input.lower() == "yes"
print("Data type:", type(is_employed))

print("\n--- Worker Profile ---")
print("Name     :", worker_name)
print("Code     :", worker_code)
print("Wage     :", wage)
print("Division :", division)
print("Employed :", is_employed)