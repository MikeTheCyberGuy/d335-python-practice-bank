# File: d335_totals_sum_practice.py

"""
Written by Michael Briley.
D335 Practice Question – Total Sum from File

Topic Area:
- File I/O, lists, numeric conversion, and aggregation.
  In this problem, you will practice:
    * Using input() to get a filename from the user.
    * Opening a text file and reading its contents.
    * Converting string data from a file into float values.
    * Using sum() to compute the total of a list of numbers.
    * Formatting numeric output to two decimal places with f-strings.
    * Appending a formatted result line back to the file.
    * Printing the full file contents to the console.

Write a Python program that:

1. Prompts the user to input the name of a text file.

   The file contains one numeric value per line, representing individual totals.
   These values may have decimal points.

   Example contents of a file named totals.txt:
       10.50
       23.40
       5.10

2. Your program must:
   - Open the file and read all of the lines.
   - Strip whitespace/newlines from each line.
   - Convert each line to a float.
   - Compute the sum of all the values.
   - Build a line in this exact format, with the total shown to two decimal places:

       Total: 39.00

3. Append that line to the *end* of the file.

4. Finally, print the entire contents of the file. For the example above,
   after your program runs, the file contents and printed output should look like:

       10.50
       23.40
       5.10
       Total: 39.00


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
#   - Use input() to ask the user for the filename.
#   - Use open(..., "r") and .readlines() to read all the lines.
#   - Strip each line (e.g. with .strip()) to remove "\n" and spaces.
#   - Convert each cleaned line to float and store in a list.
#   - Use sum(...) to compute the total of the list.
#   - Use an f-string with :.2f to format the total to two decimal places.
#   - Open the file again in append mode ("a") and write:
#         Total: <your formatted total>\n
#   - Re-open and print the file contents at the end.

# Example starting point (you can delete/change this as needed):
# filename = input("Enter filename:\n")
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
    """Reference implementation for the Total Sum from File practice question."""

    # Prompt the user to enter the filename.
    # Example input: totals.txt
    # input() returns a string, which is exactly what open() expects.
    filename = input("Enter filename.\n")

    # Open the file in read mode ("r") to get the existing numeric values.
    with open(filename, "r") as f:
        # .readlines() loads all lines into a list of strings.
        # Example: ["10.50\n", "23.40\n", "5.10\n"]
        contents = f.readlines()

    # Strip whitespace/newlines from each line and convert to float.
    # content.strip() removes the trailing "\n" and any extra spaces.
    # float(...) converts the cleaned string into a floating-point number.
    #
    # After this comprehension, for the example above we would get:
    #   [10.50, 23.40, 5.10]
    totals = [float(content.strip()) for content in contents]

    # Compute the total sum of all values in the list.
    # sum(totals) adds all the float values together.
    total_sum = sum(totals)

    # Now we want to append a new line with the total to the end of the file.
    # Open the file again in append mode ("a").
    # Append mode does not erase existing contents; it only adds at the end.
    with open(filename, "a") as f:
        # Use an f-string to format the total to exactly two decimal places.
        # total_sum:.2f ensures output like "39.00" instead of "39.0" or "39".
        #
        # We include a trailing "\n" so the file ends with a newline.
        f.write(f"Total: {total_sum:.2f}\n")

    # Finally, re-open the file in read mode and print ALL of its contents
    # so the user can see both the original numbers and the new Total line.
    with open(filename, "r") as f:
        # .read() returns the entire file contents as a single string.
        print(f.read())


# Uncomment this line temporarily if you want to directly run the reference solution:
# reference_solution()
