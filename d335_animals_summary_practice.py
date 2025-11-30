# File: d335_animals_summary_practice.py

"""
Written by Michael Briley.
D335 Practice Question – Animal List Summary

Topic Area:
- File I/O, lists, and string joining.
  In this problem, you will practice:
    * Opening and reading from a text file.
    * Stripping newline characters and extra whitespace.
    * Storing file lines in a list.
    * Using ', '.join(list) to build a comma-separated string.
    * Appending a formatted summary line back to the file.
    * Printing the entire file contents to the console.

Write a Python program that:

1. Works with a text file named: Animals.txt

   The file contains one animal name per line.
   Example contents of Animals.txt:
       Cat
       Dog
       Horse

2. Your program must:
   - Open the file and read all of the lines.
   - Strip whitespace/newlines from each line.
   - Store the cleaned animal names in a list.
   - Build a single sentence-like summary string using ', '.join(...)
     in this exact format:

       Animals: Cat, Dog, Horse

3. Append that summary line to the *end* of the file.

4. Finally, print the entire contents of the file. For the example above,
   after your program runs, the file contents and printed output should look like:

       Cat
       Dog
       Horse
       Animals: Cat, Dog, Horse


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
#   - Use a variable for the file name, e.g. filename = "Animals.txt"
#   - Use open(..., "r") and .readlines() to read all the lines.
#   - Strip each line (e.g. with .strip()) to remove "\n" and spaces.
#   - Store the cleaned lines in a list called words/animals (or similar).
#   - Use ', '.join(your_list) to build a single string of all animal names.
#   - Open the file again in append mode ("a") and write:
#         Animals: <your joined string>\n
#   - Re-open and print the file contents at the end.

# Example starting point (you can delete/change this as needed):
# filename = "Animals.txt"
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
    """Reference implementation for the Animal List Summary practice question."""

    # Name of the file we are going to read from and write to.
    # This file is expected to already exist in the same folder as this script.
    filename = "Animals.txt"

    # Open the file in read mode ("r") to get the existing animal names.
    with open(filename, "r") as f:
        # .readlines() loads all lines into a list of strings.
        # Example: ["Cat\n", "Dog\n", "Horse\n"]
        contents = f.readlines()

    # Strip whitespace/newlines from each line.
    # content.strip() removes the trailing "\n" and any extra spaces.
    # After this, we might get: ["Cat", "Dog", "Horse"]
    words = [content.strip() for content in contents]

    # Build a single comma-separated sentence from the list of animal names.
    # ', '.join(words) takes the list and creates:
    #   "Cat, Dog, Horse"
    sentence = ", ".join(words)

    # Now we want to append a new summary line to the end of the file.
    # Open the file again in append mode ("a") so we don't overwrite anything.
    with open(filename, "a") as f:
        # We write the summary in the format:
        #   Animals: Cat, Dog, Horse
        #
        # We add a trailing "\n" so that the file ends with a newline.
        # We do NOT add a leading "\n" here; we rely on the existing file
        # already ending with a newline after the last animal name.
        f.write(f"Animals: {sentence}\n")

    # Finally, re-open the file in read mode and print ALL of its contents
    # so the user can see both the original animal list and the new summary line.
    with open(filename, "r") as f:
        print(f.read())


# Uncomment this line temporarily if you want to directly run the reference solution:
# reference_solution()