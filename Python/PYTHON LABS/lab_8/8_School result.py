print("=" * 50)
print("         EXAM RESULT GENERATOR")
print("=" * 50)

# Accept pupil details
pupil_name = input("Enter Pupil Name: ")
roll_number = input("Enter Roll Number: ")

# Input scores for 5 subjects
subject_scores = []
print("\n--- Enter Scores out of 100 ---")

for subject_no in range(1, 6):
    score = int(input(f"Enter score for Subject {subject_no}: "))

    if score < 0 or score > 100:
        print("Invalid score! Enter a score between 0 and 100.")
        exit()

    subject_scores.append(score)

# Calculate total and percentage
total_score = sum(subject_scores)
percent = (total_score / 500) * 100

# Decide outcome and grade
if any(score < 40 for score in subject_scores):
    outcome = "FAIL"
    grade_letter = "F"
    comment = "Did not pass in one or more subjects"

elif percent >= 90:
    outcome = "PASS"
    grade_letter = "A+"
    comment = "Outstanding"

elif percent >= 80:
    outcome = "PASS"
    grade_letter = "A"
    comment = "Excellent"

elif percent >= 70:
    outcome = "PASS"
    grade_letter = "B"
    comment = "Very Good"

elif percent >= 60:
    outcome = "PASS"
    grade_letter = "C"
    comment = "Good"

elif percent >= 50:
    outcome = "PASS"
    grade_letter = "D"
    comment = "Satisfactory"

else:
    outcome = "PASS"
    grade_letter = "E"
    comment = "Just Passed"

# Show the report
print("\n" + "=" * 50)
print("            PUPIL PROGRESS REPORT")
print("=" * 50)

print("Pupil Name   :", pupil_name)
print("Roll Number  :", roll_number)
print("-" * 50)
print("Total Score  :", total_score, "/ 500")
print("Percentage   :", f"{percent:.1f}%")
print("Outcome      :", outcome)
print("Grade        :", grade_letter)
print("Comments     :", comment)

print("=" * 50)