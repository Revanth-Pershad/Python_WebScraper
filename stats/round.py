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

# Initialize counters for SGPA, SGPA Fail, and Others
sgpa_count = 0
sgpa_fail_count = 0
others_count = 0

# Iterate over each object in the data
for obj in data:
    obj_data = obj['data']

    # Check if the "SGPA" field exists in the data
    if "SGPA" in obj_data:
        sgpa = obj_data["SGPA"]
        if sgpa == "":
            sgpa_count += 1
        elif sgpa == "Fail":
            sgpa_fail_count += 1
        else:
            others_count += 1

# Prepare data for the pie chart
labels = ['SGPA (Pass)', 'SGPA (Fail)', 'Others']
sizes = [sgpa_count, sgpa_fail_count, others_count]

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title("Distribution of SGPA (Pass), SGPA (Fail), and Others")

plt.show()
