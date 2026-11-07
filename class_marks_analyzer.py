
# Class Marks Analyzer

# This function validates the number of students.
def get_student_count():
    while True:
        try:
            count = int(input("Enter number of students: "))

            if count > 0:
                return count
            else:
                print("Please enter at least 1 student.")

        except ValueError:
            print("Invalid input! Enter a whole number.")


# This function validates marks between 0 and 100.
def get_valid_marks(name):
    while True:
        try:
            marks = float(input(f"Enter marks for {name}: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# This function displays students who scored above average.
def display_above_average(student_names, student_marks, average):
    print("\nStudents Above Class Average:")
    found = False

    for i in range(len(student_marks)):
        if student_marks[i] > average:
            print(f"{student_names[i]} - {student_marks[i]}")
            found = True

    if not found:
        print("No student scored above the class average.")


# This function displays students with the highest and lowest marks.
def display_highest_lowest(student_names, student_marks):
    highest = max(student_marks)
    lowest = min(student_marks)

    print("\nHighest Marks:", highest)
    print("Student(s) with highest marks:")

    for i in range(len(student_marks)):
        if student_marks[i] == highest:
            print(student_names[i])

    print("\nLowest Marks:", lowest)
    print("Student(s) with lowest marks:")

    for i in range(len(student_marks)):
        if student_marks[i] == lowest:
            print(student_names[i])


# Main program starts here.

print("===================================")
print("        CLASS MARKS ANALYZER")
print("===================================")

# Create two separate lists.
student_names = []
student_marks = []

# Ask for the number of students.
number_of_students = get_student_count()

# Input student names and marks.
for i in range(number_of_students):

    print(f"\nEnter details for Student {i + 1}")

    name = input("Enter student name: ").strip().title()

    while name == "":
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip().title()

    marks = get_valid_marks(name)

    # Store names and marks in their respective lists.
    student_names.append(name)
    student_marks.append(marks)


# Calculate class statistics.
total_marks = sum(student_marks)
class_average = total_marks / len(student_marks)

# Count passing and failing students.
passing_students = 0
failing_students = 0

for marks in student_marks:
    if marks >= 50:
        passing_students += 1
    else:
        failing_students += 1


# Display class report.
print("\n===================================")
print("          CLASS REPORT")
print("===================================")

print(f"Total Students : {len(student_names)}")
print(f"Total Marks    : {total_marks:.2f}")
print(f"Class Average  : {class_average:.2f}")

# Display highest and lowest marks.
display_highest_lowest(student_names, student_marks)

# Display passing and failing students.
print("\nPassing Students:", passing_students)
print("Failing Students:", failing_students)

# Display students above average.
display_above_average(student_names, student_marks, class_average)

# Sort marks from highest to lowest.
sorted_marks = sorted(student_marks, reverse=True)

print("\nMarks Sorted (Highest to Lowest):")
print(sorted_marks)

print("===================================")
print("       ANALYSIS COMPLETED")
print("===================================")
