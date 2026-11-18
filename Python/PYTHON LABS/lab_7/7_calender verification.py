print("=" * 48)
print("         LEAP YEAR CHECKER")
print("=" * 48)

# Get the year from the user
input_year = int(input("Enter the year: "))

# Validate the input
if input_year <= 0:
    print("Error: Year must be greater than zero.")
else:
    # Decide whether it is a leap year
    if input_year % 400 == 0:
        year_type = "LEAP YEAR"
        explanation = "Century year that is divisible by 400"
        february_days = 29
        days_in_year = 366

    elif input_year % 100 == 0:
        year_type = "NORMAL YEAR"
        explanation = "Century year that is not divisible by 400"
        february_days = 28
        days_in_year = 365

    elif input_year % 4 == 0:
        year_type = "LEAP YEAR"
        explanation = "Divisible by 4 and not a century year"
        february_days = 29
        days_in_year = 366

    else:
        year_type = "NORMAL YEAR"
        explanation = "Not divisible by 4"
        february_days = 28
        days_in_year = 365

    # Show the results
    print("\n" + "=" * 48)
    print("Entered Year:", input_year)
    print("Year Type:", year_type)
    print("Total Days:", days_in_year, "days")
    print("February Days:", february_days, "days")
    print("Explanation:", explanation)
    print("=" * 48)