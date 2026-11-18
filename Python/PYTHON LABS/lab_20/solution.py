# Lab 20 - Activity Journal Book

log_file = "activity_journal.txt"


# Function to append log entry
def add_record(file_path, note):
    with open(file_path, "a") as f:
        f.write(note + "\n")

    print("[SUCCESS] New record saved to", file_path)


# Function to display complete log
def show_records(file_path):
    with open(file_path, "r") as f:
        records = f.readlines()

    print("\n============ ACTIVITY JOURNAL BOOK ============")

    if records:
        for idx, note in enumerate(records, start=1):
            print(f"{idx}. {note.strip()}")

        print("\nTotal logged records:", len(records))
    else:
        print("No journal records found.")


# Create file with sample entries if it does not exist
try:
    with open(log_file, "x") as f:
        f.write("Server initialization completed.\n")
        f.write("Workspace inspection finished.\n")
        f.write("Firewall audit verified.\n")
except FileExistsError:
    pass


# Main program
while True:
    print("\n====================================")
    print("      WORKPLACE ACTIVITY JOURNAL")
    print("====================================")
    print("1. Add Journal Record")
    print("2. Display Complete Journal")
    print("3. Exit")

    option = input("\nEnter option (1-3): ")

    if option == "1":
        note = input("Enter journal note: ")
        add_record(log_file, note)

    elif option == "2":
        show_records(log_file)

    elif option == "3":
        print("Thank you for using the Activity Journal Book. Goodbye!")
        break

    else:
        print("Invalid option! Please try again.")
