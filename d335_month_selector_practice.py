# File: d335_month_selector_practice.py

"""
Written by Michael Briley.
D335 Practice Question – Month Selector

Topic Area:
- Lists, user input, loops, and error handling.
  In this problem, you will practice:
    * Storing constant data in a list.
    * Converting user input (strings) into integers.
    * Validating user input with range checks.
    * Using a while True loop for repeated prompting.
    * Handling bad input using try/except.
    * Using string methods like .strip() and .lower().

Write a Python program that:

1. Creates a list of month names:

       ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]

2. Repeatedly asks the user to choose a month by its index.
   The index must be an integer between 0 and 11 (inclusive), where:
       0 -> "January"
       1 -> "February"
       ...
       11 -> "December"

   Example prompt:
       "Choose a month (0 for January, 1 for February, ..., 11 for December).
        Remember: the index starts at 0."

3. If the user enters something that is:
   - Not an integer, OR
   - An integer outside the range 0–11,

   Then your program should print an error message like:
       "That's not an acceptable entry. Enter a number between 0 and 11."

   and then ask again.

4. When the user enters a valid index:
   - Print the corresponding month name.
   - Then ask:
       "Would you like to continue? Type yes or no."

   Behavior:
   - If they type "yes" (any capitalization), ask for another month.
   - If they type "no", stop the program.
   - For any other answer, print:
       "Enter yes or no."
     and then ask for a month again.

5. The program runs until the user chooses to stop.

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
#   - Start by creating the months list.
#   - Use a while True loop to keep asking for input.
#   - Use input().strip() to read the user's entry and remove extra spaces.
#   - Convert the input to int inside a try block.
#   - If the number is not between 0 and 11, print an error and continue.
#   - If valid, print months[index].
#   - Ask if they want to continue; use .strip().lower() to normalize their answer.
#   - Break the loop when they say "no".

# Example starting point (you can delete/change this as needed):
# months = ["January", "February", "March", "April", "May", "June",
#           "July", "August", "September", "October", "November", "December"]
#
# while True:
#     # Your code continues here...


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
    """Reference implementation for the Month Selector practice question."""

    # Create a list of all 12 month names.
    # Index positions:
    #   0 -> "January", 1 -> "February", ..., 11 -> "December"
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # Use an infinite loop so we can keep asking the user until they choose to stop.
    while True:
        try:
            # Prompt the user to choose a month by index.
            # input() returns a string, e.g. "3\n" -> we use .strip() to remove whitespace.
            user_input = input(
                "Choose a month (0 for January, 1 for February, ..., 11 for December).\n"
                "Remember: the index starts at 0.\n"
            ).strip()

            # Convert the cleaned string to an integer.
            # If this fails (e.g. the user types "abc"), a ValueError will be raised.
            index = int(user_input)

            # Check if the index is within the valid range 0–11.
            if index < 0 or index > 11:
                # Index is outside the list range; tell the user and restart the loop.
                print("This list is only 0 - 11. Try again.\n")
                continue

            # At this point, index is guaranteed to be between 0 and 11.
            # Access the corresponding month from the list.
            print(months[index])

            # Ask the user if they want to continue.
            # .strip() removes spaces; .lower() converts "YES", "Yes", etc. to "yes".
            answer = input("Would you like to continue? Type yes or no.\n").strip().lower()

            if answer == "yes":
                # User wants to continue; go back to the top of the while loop.
                continue
            elif answer == "no":
                # User wants to stop; break out of the loop and end the function.
                break
            else:
                # User typed something other than "yes" or "no".
                # Print an instruction and then go back to the top of the loop.
                print("Enter yes or no.\n")
                continue

        # If the user types something that cannot be converted to an int,
        # int(user_input) will raise a ValueError. If for some reason we accessed
        # an invalid index, we'd get an IndexError. We handle both here.
        except (ValueError, IndexError):
            print("That's not an acceptable entry. Enter a number between 0 and 11.\n")


# Uncomment this line temporarily if you want to directly run the reference solution:
# reference_solution()
