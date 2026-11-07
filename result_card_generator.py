
# Student Result Card Generator

# This function removes extra spaces and capitalizes the student's name.
def format_name(name):
    return name.strip().title()


# This function accepts marks and checks that they are between 0 and 100.
def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# This function calculates the percentage.
def calculate_percentage(total, max_total):
    return (total / max_total) * 100


# This function assigns a grade according to the percentage.
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


# Main program starts here.

print("===================================")
print("       STUDENT RESULT CARD")
print("===================================")

# Get and format student name.
name = format_name(input("Enter student name: "))

# Validate roll number.
while True:
    roll_number = input("Enter roll number: ").strip()

    if roll_number.isdigit():
        break
    else:
        print("Invalid roll number! Digits only.")

# Get marks in five subjects.
subjects = ["English", "Mathematics", "Physics",
            "Chemistry", "Computer Science"]

marks_list = []

for subject in subjects:
    marks = get_valid_marks(subject)
    marks_list.append(marks)

# Calculate total and percentage.
total = sum(marks_list)
max_total = 500

percentage = calculate_percentage(total, max_total)

# Check whether any subject has marks below 40.
if any(mark < 40 for mark in marks_list):
    grade = "Fail"
    result = "Fail"
else:
    grade = get_grade(percentage)
    result = "Pass"

# Display the result card.
print("\n===================================")
print("          STUDENT RESULT")
print("===================================")

print(f"Student Name : {name}")
print(f"Roll Number  : {roll_number}")

print("-----------------------------------")
print("Subject              Marks")
print("-----------------------------------")

for subject, mark in zip(subjects, marks_list):
    print(f"{subject:<20} {mark:>6.1f}")

print("-----------------------------------")
print(f"Total Marks  : {total:.1f}/500")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")
print(f"Result       : {result}")
print("===================================")
print("       RESULT CARD GENERATED")
print("===================================")
