import pandas as pd

# Read the JSON file
with open("combined.json", "r") as file:
    json_data = json.load(file)

# Create a DataFrame to store the data
data = pd.DataFrame(columns=["Roll Number", "Subject", "Grade", "Result", "Credits"])

# Iterate through the JSON data and extract the required information
for obj in json_data:
    roll_number = obj["roll_number"]
    subject_data = obj["data"]

    for subject, details in subject_data.items():
        if subject != "SGPA" and subject != "CGPA":
            grade = details["grade"]
            result = details["result"]
            credits = details["credits"]

            data = data.append({
                "Roll Number": roll_number,
                "Subject": subject,
                "Grade": grade,
                "Result": result,
                "Credits": credits
            }, ignore_index=True)

# Create a Pandas Excel writer using xlsxwriter as the engine
writer = pd.ExcelWriter("output.xlsx", engine="xlsxwriter")

# Write the DataFrame to the Excel file
data.to_excel(writer, index=False)

# Customize the worksheet and format the columns
workbook = writer.book
worksheet = writer.sheets["Sheet1"]

# Set the width of columns
worksheet.set_column("A:A", 15)
worksheet.set_column("B:B", 40)
worksheet.set_column("C:E", 15)

# Close the Pandas Excel writer and save the file
writer.save()
