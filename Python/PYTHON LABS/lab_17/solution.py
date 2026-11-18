student_data = {}

def register_student():
    reg_id = input("Enter Registration Number: ")

    if reg_id in student_data:
        print("Student already exists!")
        return

    full_name = input("Enter Student Name: ")
    student_age = int(input("Enter Age: "))
    program = input("Enter Course: ")

    scores = []
    for sub in range(3):
        score = float(input(f"Enter marks in Subject {sub+1}: "))
        scores.append(score)

    student_data[reg_id] = {
        "name": full_name,
        "age": student_age,
        "course": program,
        "marks": scores
    }

    print("Student added successfully!")


def show_students():
    if not student_data:
        print("No student records found.")
        return

    print("\n---- All Student Records ----")

    for reg_id, info in student_data.items():
        total_marks = sum(info["marks"])
        avg_percent = total_marks / len(info["marks"])

        print("\nRegistration No:", reg_id)
        print("Name:", info["name"])
        print("Age:", info["age"])
        print("Course:", info["course"])
        print("Marks:", info["marks"])
        print("Percentage:", avg_percent)


def find_student():
    reg_id = input("Enter Registration Number to search: ")

    if reg_id in student_data:
        print("Student Found!")
        print(student_data[reg_id])
    else:
        print("Student not found.")


def modify_student():
    reg_id = input("Enter Registration Number to update: ")

    if reg_id in student_data:
        student_data[reg_id]["name"] = input("Enter New Name: ")
        student_data[reg_id]["age"] = int(input("Enter New Age: "))
        student_data[reg_id]["course"] = input("Enter New Course: ")

        print("Student record updated successfully!")
    else:
        print("Student not found.")


def remove_student():
    reg_id = input("Enter Registration Number to delete: ")

    if reg_id in student_data:
        del student_data[reg_id]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


while True:
    print("\n======= LEARNER DATABASE MANAGEMENT SYSTEM =======")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    option = input("Enter your option: ")

    if option == "1":
        register_student()

    elif option == "2":
        show_students()

    elif option == "3":
        find_student()

    elif option == "4":
        modify_student()

    elif option == "5":
        remove_student()

    elif option == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
