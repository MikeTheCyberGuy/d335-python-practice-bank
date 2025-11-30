# File: d335_file_stats_practice.py

"""
Written by Michael Briley.
D335 Practice Question – File Statistics

Topic Area:
- File I/O and basic data processing.
  In this problem, you will practice:
    * Using input() to get a filename from the user.
    * Opening a text file and reading its contents.
    * Converting string data from a file into numeric types.
    * Computing simple statistics (min, max, average).
    * Appending a formatted result line back to the same file.
    * Printing the full file contents to the console.

Write a Python program that:

1. Prompts the user to input the name of a text file (e.g., Scores.txt).

   The file contains exactly five lines, each with a single integer test score.
   Example contents:
       85
       92
       76
       88
       95

2. Your program must:
   - Read all five scores from the file.
   - Convert them to integers (or floats).
   - Compute:
       * The minimum score
       * The maximum score
       * The average score (as a float)

3. Construct a new line in this exact format:
       Stats: min=76, max=95, avg=87.20

4. Append that line to the *end* of the file.

5. Finally, print the entire contents of the file. For the example above,
   the printed output after your program runs should be:

       85
       92
       76
       88
       95
       Stats: min=76, max=95, avg=87.20


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
#   - Use input() to get the file name.
#   - Use open(..., "r") and .readlines() to read all the lines.
#   - Convert each line to a number (int or float).
#   - Use min(), max(), sum(), and len() for the statistics.
#   - Use f-strings to format: Stats: min=..., max=..., avg=...
#   - Append to the file using open(..., "a").
#   - Re-open and print the file contents at the end.

# Example starting point (you can delete/change this as needed):
# filename = input("Input your file name here: ")
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
    """Reference implementation for the File Statistics practice question."""

    # Ask the user for the file name.
    # Example input: Scores.txt
    # input() always returns a string, which is exactly what open() needs.
    filename = input("Input your file name here: ")

    # Open the file in read mode ("r") so we can see the existing scores.
    # The "with" statement automatically closes the file when the block ends.
    with open(filename, "r") as f:
        # .readlines() reads the entire file into a list of strings.
        # Each element is one line, including the trailing newline character "\n".
        contents = f.readlines()

    # Convert each line from a string (like "85\n") into a number (float).
    # content.strip() removes whitespace, including "\n".
    # float(...) turns "85" into 85.0, "92" into 92.0, etc.
    numbers = [float(content.strip()) for content in contents]

    # Compute basic statistics using Python's built-in functions.
    # min() -> smallest value in the list.
    min_score = min(numbers)

    # max() -> largest value in the list.
    max_score = max(numbers)

    # sum(numbers) -> total of all scores.
    # len(numbers) -> how many scores we have.
    # Dividing gives us the average as a float.
    avg_score = sum(numbers) / len(numbers)

    # Now we want to APPEND a new line to the file with our stats.
    # We open the same file again, this time in append mode ("a").
    # Append mode does NOT erase the existing contents; it adds to the end.
    with open(filename, "a") as f:
        # We use an f-string (formatted string literal) to build the line
        # exactly in the required format:
        #   Stats: min=76, max=95, avg=87.20
        #
        # int(min_score) and int(max_score) remove the .0 part so they
        # print like integers (76, not 76.0).
        #
        # avg_score:.2f formats the average to exactly 2 decimal places.
        # For example, 87.2 becomes "87.20".
        #
        # Note: we are not adding a leading "\n" here. This assumes that the
        # last existing line in the file already ends with a newline, so our
        # "Stats: ..." text will start on a new line.
        f.write(f"Stats: min={int(min_score)}, max={int(max_score)}, avg={avg_score:.2f} ")

    # Finally, we re-open the file in read mode and print EVERYTHING,
    # so the user can see both the original scores and the new Stats line.
    with open(filename, "r") as f:
        # .read() reads the entire file as one big string.
        # print() sends that string to the console.
        print(f.read())


# Uncomment this line temporarily if you want to directly run the reference solution:
# reference_solution()
