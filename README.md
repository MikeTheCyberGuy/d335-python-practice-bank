# D335 Python Practice Bank

A small collection of self-contained Python practice problems inspired by the kinds of tasks you’ll see in an intro programming / CS fundamentals course.

## Code of Conduct

By using or contributing to this repository, you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).  
In short: this repo is for practice-only content, **not** for sharing exam answers or graded assignment solutions.

Each file is designed so that students can:

- Read a clear problem statement at the top.
- Work in a “student solution” area.
- Compare against a reference solution (usually wrapped in a function) when they’re ready.

The focus is on:
- Basic I/O
- File handling
- Lists and indexing
- Type inspection and conditionals
- Simple numeric processing and formatting

---

## Repository name

Suggested repo name (what this README assumes):

`d335-python-practice-bank`

You can, of course, rename it to whatever fits your environment.

---

## Contents

Current files expected in this repo:

- **`d335_month_selector_practice.py`**  
  Practice using lists, input, loops, and basic error handling. Students choose a month index and the program prints the corresponding month name, optionally with validation.

- **`d335_student_info_practice.py`**  
  Reads simple student information from a text file (first name, last name, major) and appends a formatted summary line such as:  
  `Student: John Smith - Major: Computer Science`

- **`d335_totals_sum_practice.py`**  
  Reads numeric values (e.g., expenses) from a text file, converts lines to `float`, computes the total, and appends a line like:  
  `Total: 39.00`  
  Good for practicing file reading, list comprehensions, numeric conversion, and `:.2f` formatting.

- **`d335_animals_summary_practice.py`**  
  Works with a small text file containing animal names and appends a sentence summarizing them on a single line. Reinforces `readlines()`, `.strip()`, and `" ".join(...)`.

- **`d335_courses_offered_practice.py`**  
  Similar to the animals exercise, but with course names. Builds a line such as:  
  `Courses offered: Math, Science, History`

- **`d335_file_stats_practice.py`**  
  Reads several numeric scores from a file, computes min, max, and average, and appends a stats line like:  
  `Stats: min=76, max=95, avg=87.20`  
  Reinforces numeric processing, `min()`, `max()`, `sum()/len()`, and formatted output.

- **`d335_type_classifier_practice.py`**  
  Uses a mixed list of values and an index from the user to:
  - Retrieve an element
  - Inspect its type using `type(...).__name__`
  - Classify the element as iterable, numeric, or “other”
  Great for practicing `isinstance`, type inspection, and conditional logic.

- **`data_mixture.py`**  
  A small helper/module that may contain the shared `data_mixture` list for type-classification exercises (or similar shared data for other problems).

---

## Getting started

### 1. Clone the repo

On your machine:

```bash
git clone https://github.com/MikeTheCyberGuy/d335-python-practice-bank.git
cd d335-python-practice-bank