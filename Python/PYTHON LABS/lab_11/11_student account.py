user_id = input("Enter your user ID: ")
secret_key = input("Enter your password: ")

# Password validation rules
has_min_length = len(secret_key) >= 10
has_number = any(ch.isdigit() for ch in secret_key)
has_capital = any(ch.isupper() for ch in secret_key)

print("\n" + "=" * 44)
print("        ACCOUNT SECURITY CHECK")
print("=" * 44)

print("User ID :", user_id)
print("Password:", "*" * len(secret_key))

print("\n--- Security Requirements ---")

if has_min_length:
    print("[PASS] Minimum 10 characters")
else:
    print("[FAIL] Minimum 10 characters")

if has_number:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if has_capital:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

print("\n" + "=" * 44)

# Final result
if has_min_length and has_number and has_capital:
    print("Password is ACCEPTED!")
    print(f"Profile registered successfully for {user_id}!")
else:
    print("Password is REJECTED!")
    print("Please try again with a stronger password.")

print("=" * 44)
