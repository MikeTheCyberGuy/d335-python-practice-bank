# File: d335_type_classifier_practice.py

"""
Written by Michael Briley.
D335 Practice Question – Type Classifier

Topic Area:
- Lists, indexing, type inspection, conditionals, and input validation.
  In this problem, you will practice:
    * Storing different kinds of objects in a single list.
    * Accessing list elements by index.
    * Using type() and .__name__ to get an object's type.
    * Classifying objects based on their type (iterable vs numeric vs other).
    * Validating user input (range checks and conversion to int).
    * Using a while True loop and try/except for robust error handling.

Write a Python program that:

1. Starts with the following list of mixed-type items:

       items = [
           "Hello, world!",      # str
           123,                  # int
           3.14,                 # float
           [1, 2, 3],            # list
           {"a": 1, "b": 2},     # dict
           (10, 20),             # tuple
           None                  # NoneType
       ]

2. Repeatedly asks the user to enter an index from 0 to 6 (inclusive) to select
   one of the items from the list.

   Example prompt:
       "Input a number between 0 and 6 to figure out its type."

3. When the user enters an index:
   - If the input is not a valid integer, print an error message like:
         "That's not an acceptable entry. Enter a number between 0 and 6."
     and ask again.
   - If the integer is outside the range 0–6, print:
         "Enter a number between 0 and 6 to find the object type and more."
     and ask again.

4. When the user enters a valid index (0–6), determine the type of the
   corresponding item using type(item).__name__ and then:

   - If the item is a string, list, dict, or tuple, print:
         "The <item> is a <type> type and is iterable."
   - If the item is an int or float, print:
         "The <item> is a <type> type and is numeric."
   - For anything else (e.g., NoneType), print:
         "The <item> is a <type> type."

   After printing the message for a valid index, the program should exit.

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
#   - Start by defining the items list exactly as in the description.
#   - Use a while True loop to keep asking for an index until you get valid input.
#   - Use input().strip() to read the user's entry and remove extra spaces.
#   - Convert the input to int inside a try block to catch ValueError.
#   - Check that the index is between 0 and 6 (inclusive) before using it.
#   - Use type(item).__name__ to get the type name as a string.
#   - Use if/elif/else to decide whether to label it "iterable", "numeric", or "other".
#   - After printing the appropriate message for a valid index, break the loop.

# Example starting point (you can delete/change this as needed):
# items = [
#     "Hello, world!",      # str
#     123,                  # int
#     3.14,                 # float
#     [1, 2, 3],            # list
#     {"a": 1, "b": 2},     # dict
#     (10, 20),             # tuple
#     None                  # NoneType
# ]
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
    """Reference implementation for the Type Classifier practice question."""

    # Define a list containing different kinds of Python objects.
    # We will let the user pick one of these by index.
    items = [
        "Hello, world!",      # str
        123,                  # int
        3.14,                 # float
        [1, 2, 3],            # list
        {"a": 1, "b": 2},     # dict
        (10, 20),             # tuple
        None                  # NoneType
    ]

    while True:
        try:
            # Ask the user to enter an index.
            # input() returns a string; .strip() removes surrounding whitespace.
            user_input = input("Input a number between 0 and 6 to figure out its type.\n").strip()

            # Convert the user input to an integer.
            # If this fails (e.g. "abc"), ValueError is raised and caught below.
            index = int(user_input)

            # Check if the index is within the valid range for our list.
            if index < 0 or index > 6:
                # The index is out of range; tell the user and continue the loop.
                print("Enter a number between 0 and 6 to find the object type and more.\n")
                continue

            # At this point, index is between 0 and 6, so it's safe to index the list.
            item = items[index]

            # type(item) returns the type object, e.g. <class 'int'>.
            # .__name__ gives us the name as a string, e.g. "int".
            item_type = type(item).__name__

            # Classify the item as iterable, numeric, or other.
            if item_type in ("str", "list", "dict", "tuple"):
                # These types are commonly considered iterable in Python.
                print(f"The {item} is a {item_type} type and is iterable.")
                break
            elif item_type in ("int", "float"):
                # These types represent numeric values.
                print(f"The {item} is a {item_type} type and is numeric.")
                break
            else:
                # For any other type (e.g. NoneType), just print the type name.
                print(f"The {item} is a {item_type} type.")
                break

        except ValueError:
            # int(user_input) failed because the input was not a valid integer.
            print("That's not an acceptable entry. Enter a number between 0 and 6.\n")


# Uncomment this line temporarily if you want to directly run the reference solution:
# reference_solution()