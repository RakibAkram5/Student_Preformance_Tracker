# LMS Project in Python
======================================
### Overview
--------------------------------------
Here's a step-by-step breakdown of each function in the code, organized by numbered steps:

### `Student` Class

1. **`__init__(self, name, scores)`**:
   - Step 1: Accept the `name` (student's name) and `scores` (list of scores) as inputs.
   - Step 2: Assign the `name` to the `self.name` attribute.
   - Step 3: Assign the `scores` to the `self.scores` attribute.

2. **`calculate_average(self)`**:
   - Step 1: Use the `sum()` function to calculate the total of `self.scores`.
   - Step 2: Divide the total score by the number of scores (`len(self.scores)`).
   - Step 3: Return the result as the student's average score.

3. **`is_passing(self, passing_score=40)`**:
   - Step 1: Use the `all()` function to check if all scores in `self.scores` are greater than or equal to the `passing_score`.
   - Step 2: Return `True` if all scores are passing; otherwise, return `False`.

### `PerformanceTracker` Class

1. **`__init__(self)`**:
   - Step 1: Initialize an empty dictionary `self.students` to store students' data.

2. **`add_student(self, name, scores)`**:
   - Step 1: Create a new `Student` object using the provided `name` and `scores`.
   - Step 2: Add this student object to the `self.students` dictionary, using the student's `name` as the key.

3. **`calculate_class_average(self)`**:
   - Step 1: Initialize a variable `total` to store the sum of all students' average scores.
   - Step 2: Loop through each student object in `self.students`.
   - Step 3: For each student, call `calculate_average()` and add the result to the `total`.
   - Step 4: If there are students in the dictionary, divide the `total` by the number of students to calculate the class average.
   - Step 5: Return the class average, or `0` if there are no students.

4. **`display_student_performance(self)`**:
   - Step 1: Loop through each student object in `self.students`.
   - Step 2: For each student, call `calculate_average()` to get the average score.
   - Step 3: Call `is_passing()` to check if the student is passing.
   - Step 4: Print the student's name, average score (formatted to 2 decimal places), and passing status ("Passing" or "Failing").

### Helper Function

1. **`get_student_input()`**:
   - Step 1: Continuously prompt the user to enter the student's name, or type "done" to stop the input process.
   - Step 2: For each student, prompt the user to enter their scores for Math, Science, and English.
   - Step 3: Validate the input, ensuring the scores are numeric.
   - Step 4: If the input is valid, yield the student's name and scores.
   - Step 5: If the input is invalid (non-numeric values), display an error message and re-prompt the user.

### Main Function

1. **`main()`**:
   - Step 1: Create an instance of `PerformanceTracker`.
   - Step 2: Call `get_student_input()` to gather student names and scores from the user.
   - Step 3: For each student, call `add_student()` to add the student to the performance tracker.
   - Step 4: Call `display_student_performance()` to print the performance report of each student.
   - Step 5: Call `calculate_class_average()` to compute and print the class average score.


