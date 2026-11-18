# Lab 15 - Student Record Management Portal

# Initial Student Records
student_records = {
    201: {
        "Name": "Aarav",
        "Branch": "BTech AI",
        "Semester": 2,
        "Marks": [88, 91, 84]
    },
    202: {
        "Name": "Ananya",
        "Branch": "BTech AI",
        "Semester": 2,
        "Marks": [94, 89, 96]
    },
    203: {
        "Name": "Kabir",
        "Branch": "BTech AI",
        "Semester": 2,
        "Marks": [79, 86, 81]
    }
}


# 1. View All Students
def show_all_students():
    print("\n--- Registered Student Records ---")

    if not student_records:
        print("No student records available.")
        return

    for roll_id, info in student_records.items():
        print(
            f"Roll ID: {roll_id} | "
            f"Name: {info['Name']} | "
            f"Branch: {info['Branch']}"
        )
        print(
            f"Semester: {info['Semester']} | "
            f"Marks: {info['Marks']}"
        )

    print("Total Registered Students:", len(student_records))


# 2. Search Student by Roll Number
def find_student():
    try:
        roll_id = int(input("Enter Roll ID to search: "))

        record = student_records.get(roll_id)

        if record:
            print(f"\n[FOUND] Record for Roll ID {roll_id}:")
            print("Name:", record["Name"])
            print("Branch:", record["Branch"])
            print("Semester:", record["Semester"])
            print("Marks:", record["Marks"])
        else:
            print("[ERROR] Student record not found.")

    except ValueError:
        print("Invalid input! Enter a valid Roll ID.")


# 3. Register New Student
def add_student():
    try:
        roll_id = int(input("Enter Roll ID: "))

        if roll_id in student_records:
            print("[ERROR] Roll ID already exists!")
            return

        student_name = input("Enter Student Name: ").strip()
        dept = input("Enter Branch (e.g., BTech AI): ").strip()
        sem = int(input("Enter Semester: "))

        if not student_name or not dept:
            print("Name and Branch cannot be empty.")
            return

        if not 1 <= sem <= 8:
            print("Semester must be between 1 and 8.")
            return

        scores = []

        print("Enter marks in 3 subjects:")

        for sub in range(1, 4):
            score = int(input(f"Subject {sub}: "))

            if not 0 <= score <= 100:
                print("Marks must be between 0 and 100.")
                return

            scores.append(score)

        student_records[roll_id] = {
            "Name": student_name,
            "Branch": dept,
            "Semester": sem,
            "Marks": scores
        }

        print(
            f"\n[SUCCESS] Student '{student_name}' "
            f"(Roll ID: {roll_id}) registered successfully!"
        )

    except ValueError:
        print("Invalid input! Please enter numbers correctly.")


# 4. Update Student Details
def modify_student():
    try:
        roll_id = int(input("Enter Roll ID to update: "))

        if roll_id not in student_records:
            print("[ERROR] Student record not found.")
            return

        record = student_records[roll_id]

        print(f"Current details for Roll ID {roll_id}:")
        print("1. Branch:", record["Branch"])
        print("2. Semester:", record["Semester"])

        option = input(
            "Choose field to update (1 for Branch, 2 for Semester): "
        )

        if option == "1":
            dept = input("Enter new Branch: ").strip()

            if dept:
                record["Branch"] = dept
                print("[SUCCESS] Branch updated successfully.")
            else:
                print("Branch cannot be empty.")

        elif option == "2":
            sem = int(input("Enter new Semester: "))

            if 1 <= sem <= 8:
                record["Semester"] = sem
                print(
                    f"[SUCCESS] Semester updated to {sem}."
                )
            else:
                print("Invalid Semester!")

        else:
            print("Invalid field choice!")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


# 5. View Academic Performance
def show_academic_performance():
    try:
        roll_id = int(
            input("Enter Roll ID for Academic Performance: ")
        )

        if roll_id not in student_records:
            print("[ERROR] Student record not found.")
            return

        record = student_records[roll_id]
        scores = record["Marks"]

        total_marks = sum(scores)
        avg_marks = total_marks / len(scores)

        status = "PASS" if avg_marks >= 40 else "FAIL"

        print("\n" + "=" * 44)
        print("          PERFORMANCE SUMMARY")
        print("=" * 44)

        print(
            f"Student Name : {record['Name']} "
            f"(Roll: {roll_id})"
        )
        print("Branch       :", record["Branch"])
        print("Semester     :", record["Semester"])
        print("Subject Marks:", scores)
        print(f"Total Marks  : {total_marks} / 300")
        print(f"Average Marks: {avg_marks:.2f}%")
        print(f"Final Result : {status}")

        print("=" * 44)

    except ValueError:
        print("Invalid input! Enter a valid Roll ID.")


# 6. Delete Student Record
def remove_student():
    try:
        roll_id = int(input("Enter Roll ID to delete: "))

        deleted_record = student_records.pop(roll_id, None)

        if deleted_record is not None:
            print(
                f"\n[SUCCESS] Record for "
                f"'{deleted_record['Name']}' "
                f"(Roll ID: {roll_id}) deleted successfully."
            )
        else:
            print("[ERROR] Student record not found.")

    except ValueError:
        print("Invalid input! Enter a valid Roll ID.")


# Main Menu
def start_portal():
    while True:
        print("\n" + "=" * 48)
        print("     STUDENT RECORD MANAGEMENT PORTAL")
        print("=" * 48)

        print("\nSelect an operation:")
        print("1. View All Students")
        print("2. Search Student by Roll ID")
        print("3. Register New Student")
        print("4. Update Student Details")
        print("5. View Academic Performance")
        print("6. Delete Student Record")
        print("7. Exit")

        option = input("\nEnter your choice (1-7): ")

        if option == "1":
            show_all_students()

        elif option == "2":
            find_student()

        elif option == "3":
            add_student()

        elif option == "4":
            modify_student()

        elif option == "5":
            show_academic_performance()

        elif option == "6":
            remove_student()

        elif option == "7":
            print(
                "\nThank you for using Student "
                "Record Portal. Goodbye!"
            )
            break

        else:
            print("[ERROR] Invalid choice! Please select 1-7.")


# Execute Program
if __name__ == "__main__":
    start_portal()
