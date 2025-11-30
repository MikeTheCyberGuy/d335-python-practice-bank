# File: d335_student_info_practice.py

"""
Written by Michael Briley.
D335 Practice Question – Student Info Formatting

Topic Area:
- File I/O and string formatting.
  In this problem, you will practice:
    * Opening and reading from a text file.
    * Stripping newline characters and extra whitespace.
    * Storing file lines in a list for later use.
    * Indexing into a list to access specific pieces of data.
    * Building a formatted summary string with an f-string.
    * Appending that summary to the end of the same file.
    * Printing the entire file contents to the console.

Write a Python program that:

1. Works with a text file named: StudentInfo.txt

   The file contains exactly three lines:
       - First line: the student's first name
       - Second line: the student's last name
       - Third line: the student's major

   Example contents of StudentInfo.txt:
       Michael
       Briley
       Cybersecurity

2. Your program must:
   - Open the file and read all of the lines.
   - Strip whitespace/newlines from each line.
   - Build a single summary line in this exact format:

       Student: Michael Briley - Major: Cybersecurity

3. Append that summary line to the *end* of the file.

4. Finally, print the entire contents of the file. For the example above,
   after your program runs, the file contents and printed output should look like:

       Michael
       Briley
       Cybersecurity
       Student: Michael Briley - Major: Cybersecurity


INSTRUCTIONS:
- Write your solution in the "Student Solution Area" below.
- When you are completely done and have tested your code,
  scroll down to the "Reference Solution" and compare your answer.
"""

# ============================
#   STUDENT SOLUTION AREA
# ============================

# TODO: Write your code below.
# Hints:
#   - Use a variable for the file name, e.g. filename = "StudentInfo.txt"
#   - Use open(..., "r") and .readlines() to read all the lines.
#   - Strip each line (e.g. with .strip()) to remove "\n" and spaces.
#   - Store the cleaned lines in a list so you can access:
#         first name  -> index 0
#         last name   -> index 1
#         major       -> index 2
#   - Use an f-string to build: "Student: First Last - Major: Major"
#   - Open the file again in append mode ("a") and write the summary line.
#   - Re-open and print the file contents at the end.

# Example starting point (you can delete/change this as needed):
# filename = "StudentInfo.txt"
# # Your code continues here...


# ============================
#   END OF STUDENT AREA
#   SCROLL DOWN *ONLY* AFTER
#   YOU HAVE TRIED THE PROBLEM
# ============================














# ==============================================================
#   REFERENCE SOLUTION (FOR INSTRUCTORS / SELF-CHECK ONLY)
#   Do NOT look at this until you have attempted the problem.
#   To run this solution instead of your own, you can:
#     1) Comment out your code above, and
#     2) Call reference_solution()
# ==============================================================

def reference_solution():
    """Reference implementation for the Student Info Formatting practice question."""

    # Name of the file we are going to read from and write to.
    # This file is expected to already exist in the same folder as this script.
    filename = "StudentInfo.txt"

    # Open the file in read mode ("r") to get the existing student info.
    with open(filename, "r") as f:
        # .readlines() loads all lines into a list of strings.
        # Example: ["Michael\n", "Briley\n", "Cybersecurity\n"]
        contents = f.readlines()

    # Strip whitespace/newlines from each line.
    # content.strip() removes the trailing "\n" and any extra spaces.
    # After this, we might get: ["Michael", "Briley", "Cybersecurity"]
    studentnames = [content.strip() for content in contents]

    # Now we want to append a new summary line to the end of the file.
    # Open the file again, this time in append mode ("a").
    with open(filename, "a") as f:
        # Build the summary line using an f-string.
        #
        # studentnames[0] -> first name
        # studentnames[1] -> last name
        # studentnames[2] -> major
        #
        # We add a leading "\n" so that the summary line starts on a new line
        # after the original three lines.
        #
        # Note: We call .strip() again here, which is technically redundant
        # because the list comprehension above already stripped the values,
        # but it does not hurt and keeps the data clean if the code changes.
        f.write(
            f"\nStudent: {studentnames[0].strip()} "
            f"{studentnames[1].strip()} - Major: {studentnames[2].strip()}"
        )

    # Finally, re-open the file in read mode and print ALL of its contents
    # so the user can see both the original lines and the new summary line.
    with open(filename, "r") as f:
        print(f.read())


# Uncomment this line temporarily if you want to directly run the reference solution:
# reference_solution()