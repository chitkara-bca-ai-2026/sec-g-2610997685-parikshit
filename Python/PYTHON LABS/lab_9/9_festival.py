print("=" * 38)
print("     EVENT BANNER PATTERN MAKER")
print("=" * 38)

# Take input from the user
size = int(input("Enter the number of lines: "))

if size <= 0:
    print("Please enter a valid positive number.")
else:
    # Pattern 1: Star Triangle
    print("\nDesign 1: Star Triangle")
    print("-" * 32)

    for row in range(1, size + 1):
        for col in range(row):
            print("*", end=" ")
        print()

    # Pattern 2: Number Triangle
    print("\nDesign 2: Number Triangle")
    print("-" * 32)

    for row in range(1, size + 1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()

    # Pattern 3: Inverted Star Triangle
    print("\nDesign 3: Inverted Star Triangle")
    print("-" * 32)

    for row in range(size, 0, -1):
        for col in range(row):
            print("*", end=" ")
        print()

    # Pattern 4: Pyramid
    print("\nDesign 4: Pyramid")
    print("-" * 32)

    for row in range(1, size + 1):
        print(" " * (size - row), end="")
        print("* " * (row * 2 - 1))
