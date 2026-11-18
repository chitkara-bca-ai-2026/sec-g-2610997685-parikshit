import os

# Function to write notes
def write_notes(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    print("Notes successfully saved to", filename)


# Function to read notes
def read_notes(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.read()

        if content:
            print("\n--- Saved Notes ---")
            print(content)
        else:
            print("No notes found in the file.")
    else:
        print("No notes file exists yet.")


# Main program
filename = "notes.txt"

while True:
    print("\n==============================")
    print("  STUDENT NOTES MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        content = input("Enter notes to save: ")
        write_notes(filename, content)

    elif choice == "2":
        read_notes(filename)

    elif choice == "3":
        print("Thank you for using the Student Notes Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")