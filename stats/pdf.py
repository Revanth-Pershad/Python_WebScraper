import json
from tabulate import tabulate
from fpdf import FPDF
import os

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the file path to the JSON file
json_file_path = os.path.join(current_directory, "combined.json")

# Read JSON data from file
with open(json_file_path, "r") as file:
    json_data = json.load(file)

# Extract the relevant data
table_data = []
for item in json_data:
    roll_number = item['roll_number']
    grades = []
    for subject, subject_data in item['data'].items():
        grade = subject_data
        grades.append(grade)
    table_data.append([roll_number] + grades)

# Create PDF document
pdf = FPDF()
pdf.add_page()

# Define table headers
headers = ['Roll Number'] + list(json_data[0]['data'].keys())

# Add table to PDF
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Grades Report', 0, 1, 'C')
pdf.ln(5)

pdf.set_font('Arial', '', 10)
pdf.cell(0, 10, tabulate(table_data, headers, tablefmt='grid'), 0, 1)

# Save PDF file
pdf.output('grades_report.pdf')
