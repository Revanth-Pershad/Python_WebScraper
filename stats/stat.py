# import json
# import os

# # Get the current directory
# current_directory = os.path.dirname(os.path.abspath(__file__))

# # Construct the file path to the JSON file
# json_file_path = os.path.join(current_directory, "combined.json")

# # Read JSON data from file
# with open(json_file_path, "r") as file:
#     data = json.load(file)

# # Initialize a dictionary to store the grade counts for each object
# grade_counts = {}

# # Iterate over each object in the data
# for obj in data:
#     roll_number = obj['roll_number']
#     obj_data = obj['data']

#     # Iterate over each subject in the object's data
#     for subject, details in obj_data.items():
#         if subject not in grade_counts:
#             grade_counts[subject] = {}

#         # Check if the 'grade' attribute exists in the details
#         if 'grade' in details:
#             # Extract the grade for the subject
#             grade = details['grade']

#             # Update the count for the grade in the grade_counts dictionary
#             if grade not in grade_counts[subject]:
#                 grade_counts[subject][grade] = 0
#             grade_counts[subject][grade] += 1

# # Print the grade counts for each subject
# for subject, counts in grade_counts.items():
#     print(f"Subject: {subject}")
#     for grade, count in counts.items():
#         print(f"Grade {grade}: {count} students")
#     print()


import json
import os
import matplotlib.pyplot as plt

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the file path to the JSON file
json_file_path = os.path.join(current_directory, "combined.json")

# Read JSON data from file
with open(json_file_path, "r") as file:
    data = json.load(file)

# Initialize a dictionary to store the grade counts for each object
grade_counts = {}

# Iterate over each object in the data
for obj in data:
    roll_number = obj['roll_number']
    obj_data = obj['data']

    # Iterate over each subject in the object's data
    for subject, details in obj_data.items():
        if subject not in grade_counts:
            grade_counts[subject] = {}

        # Check if the 'grade' attribute exists in the details
        if 'grade' in details:
            # Extract the grade for the subject
            grade = details['grade']

            # Update the count for the grade in the grade_counts dictionary
            if grade not in grade_counts[subject]:
                grade_counts[subject][grade] = 0
            grade_counts[subject][grade] += 1

# Create bar plots for each subject
for subject, counts in grade_counts.items():
    grades = list(counts.keys())
    count_values = list(counts.values())

    # Create a bar plot
    plt.bar(grades, count_values)

    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title(f"Grade Distribution for {subject}")
    plt.show()
