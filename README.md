# Functions, Strings and Lists – Python Assessment

## 1. Project Overview

This project contains two Python programs developed as part of the **Functions, Strings and Lists** assessment. The programs demonstrate the use of Python functions, strings, lists, loops, conditional statements, input validation, and built-in functions.

Both programs are designed to manage and analyze student academic results through user input and display organized output.

## 2. Description of Programs

### Task 1: Student Result Card Generator

This program generates an individual student's result card by collecting their name, roll number, and marks in five subjects.

**Main Features:**
- Accepts student name, roll number, and marks in five subjects.
- Validates roll number using `.isdigit()`.
- Validates subject marks within the range of 0–100.
- Formats the student's name using `.strip()` and `.title()`.
- Calculates total marks and percentage.
- Assigns grades according to the percentage:
  - 90 and above: A+
  - 80–89: A
  - 70–79: B
  - 60–69: C
  - 50–59: D
  - Below 50: Fail
- Declares the student Fail if any subject has marks below 40, regardless of the overall percentage.
- Displays a formatted result card using f-strings.

**Functions Used:**

| Function | Description |
|---|---|
| `format_name(name)` | Removes extra spaces and capitalizes the student's name. |
| `get_valid_marks(subject)` | Accepts and validates marks between 0 and 100. |
| `calculate_percentage(total, max_total)` | Calculates the student's percentage. |
| `get_grade(percentage)` | Determines the grade according to the percentage. |

### Task 2: Class Marks Analyzer

This program analyzes the academic performance of an entire class by collecting student names and their marks.

**Main Features:**
- Asks the user for the number of students.
- Creates two separate lists: `student_names` and `student_marks`.
- Uses `.append()` to store student names and marks.
- Validates student marks within the range of 0–100.
- Calculates the class average using `sum()` and `len()`.
- Identifies the highest and lowest marks using `max()` and `min()`.
- Displays all students who achieved the highest and lowest marks.
- Counts passing students (50 or above) and failing students (below 50).
- Displays students who scored above the class average.
- Sorts student marks from highest to lowest using `sorted()`.

**Functions Used:**

| Function | Description |
|---|---|
| `get_student_count()` | Accepts and validates the number of students. |
| `get_valid_marks(name)` | Accepts and validates student marks. |
| `display_above_average(student_names, student_marks, average)` | Displays students scoring above the class average. |
| `display_highest_lowest(student_names, student_marks)` | Displays the highest and lowest marks and the students who achieved them. |

## 3. Python Concepts and Functions Used

The following Python concepts are implemented across both programs:

| Concept / Function | Usage |
|---|---|
| `def` | Defines custom functions. |
| Parameters | Pass values into functions. |
| `return` | Returns calculated or validated values. |
| Strings | Stores and processes student names and roll numbers. |
| `.strip()` | Removes extra spaces from strings. |
| `.title()` | Capitalizes the first letter of each word. |
| `.isdigit()` | Checks whether the roll number contains only digits. |
| Lists `[]` | Stores student names and marks. |
| `.append()` | Adds new elements to lists. |
| `len()` | Counts the number of students. |
| `sum()` | Calculates total marks. |
| `max()` | Finds the highest marks. |
| `min()` | Finds the lowest marks. |
| `sorted()` | Sorts marks in ascending or descending order. |
| `for` loop | Iterates through subjects and student records. |
| `while` loop | Repeats input until valid data is entered. |
| `if-elif-else` | Handles grading and result conditions. |
| `try-except` | Handles invalid numerical input. |
| `f-strings` | Displays formatted output. |
| `any()` | Checks whether any subject has marks below 40 in Task 1. |
| `zip()` | Displays subjects alongside their marks in Task 1. |

## 4. How to Run the Programs

**Requirements:**
- Python 3 installed on your computer.
- A code editor such as Visual Studio Code, IDLE, or PyCharm.

**Steps:**

1. Download or clone the project files.
2. Open the project folder in your code editor.
3. Open the terminal.
4. Run the first program:

   ```bash
   python task1.py
   ```

5. Run the second program:

   ```bash
   python task2.py
   ```

6. Enter the requested information and view the generated results.

*Note: Replace `task1.py` and `task2.py` with your actual Python filenames if they are different.*

## 5. Sample Input and Output

### Task 1: Student Result Card Generator

**Sample Input:**

```text
Enter student name: ali ahmed
Enter roll number: 1025
Enter marks for English (0-100): 85
Enter marks for Mathematics (0-100): 92
Enter marks for Physics (0-100): 78
Enter marks for Chemistry (0-100): 88
Enter marks for Computer Science (0-100): 95
```

**Sample Output:**

```text
===================================
          STUDENT RESULT
===================================
Student Name : Ali Ahmed
Roll Number  : 1025
-----------------------------------
Subject              Marks
-----------------------------------
English                85.0
Mathematics            92.0
Physics                78.0
Chemistry              88.0
Computer Science       95.0
-----------------------------------
Total Marks  : 438.0/500
Percentage   : 87.60%
Grade        : A
Result       : Pass
===================================
```

### Task 2: Class Marks Analyzer

**Sample Input:**

```text
Enter number of students: 5

Enter details for Student 1
Enter student name: Ali
Enter marks for Ali: 85

Enter details for Student 2
Enter student name: Ahmed
Enter marks for Ahmed: 45

Enter details for Student 3
Enter student name: Sara
Enter marks for Sara: 95

Enter details for Student 4
Enter student name: Ayesha
Enter marks for Ayesha: 75

Enter details for Student 5
Enter student name: Usman
Enter marks for Usman: 50
```

**Sample Output:**

```text
===================================
          CLASS REPORT
===================================
Total Students : 5
Total Marks    : 350.00
Class Average  : 70.00

Highest Marks: 95.0
Student(s) with highest marks:
Sara

Lowest Marks: 45.0
Student(s) with lowest marks:
Ahmed

Passing Students: 4
Failing Students: 1

Students Above Class Average:
Ali - 85.0
Sara - 95.0
Ayesha - 75.0

Marks Sorted (Highest to Lowest):
[95.0, 85.0, 75.0, 50.0, 45.0]

===================================
       ANALYSIS COMPLETED
===================================
```

## 6. Conclusion

Both programs successfully demonstrate the practical application of Python functions, strings, lists, loops, conditional statements, and input validation.

The Student Result Card Generator focuses on individual student performance, while the Class Marks Analyzer evaluates the performance of an entire class. Together, these programs demonstrate the use of fundamental Python programming concepts to solve practical academic problems.