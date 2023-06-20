import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://results.cvr.ac.in/cvrresults1/result.php?resid=bt12e46x060413NF'
data_array = []

for i in range(24):
    for j in range(10):
        letter = chr(ord('a') + i)

        if letter not in ('i', 'o'):
            roll_number = f'21b81a05{letter + str(j)}'
            response = requests.post(base_url, data={'srno': roll_number, 'type': 'roll', 'phase1': ''})

            if response.status_code == 200:
                html_content = response.content
                soup = BeautifulSoup(html_content, 'html.parser')

                tbody = soup.find('tbody', class_='zebra-striped')

                if tbody:
                    rows = tbody.find_all('tr')
                    data_obj = {}

                    # Find the name in the table
                    name_table = soup.find('table', class_='bttable blue')
                    if name_table:
                        name_row = name_table.find('tr', text='Name')
                        if name_row:
                            name_cell = name_row.find_next('td')
                            name = name_cell.text.strip()
                            data_obj['name'] = name

                    for row in rows:
                        cells = row.find_all('td')

                        if len(cells) == 4:
                            subject = cells[0].text.strip()
                            grade = cells[1].text.strip()
                            result = cells[2].text.strip()
                            credits = cells[3].text.strip()

                            data_obj[subject] = {
                                'grade': grade,
                                'result': result,
                                'credits': credits
                            }

                    # Find additional table based on unique text
                    additional_table = None
                    tables = soup.find_all('table')
                    for table in tables:
                        if table.find(text='SGPA') and table.find(text='CGPA'):
                            additional_table = table
                            break

                    if additional_table:
                        rows = additional_table.find_all('tr')
                        for row in rows:
                            cells = row.find_all('td')
                            if len(cells) == 2:
                                key = cells[0].text.strip()
                                value = cells[1].text.strip()
                                data_obj[key] = value

                    data_array.append({
                        'roll_number': roll_number,
                        'data': data_obj
                    })

                    print(f'Data extracted for roll number {roll_number}')
                else:
                    print(f'Unable to find tbody for roll number {roll_number}')
            else:
                print(f'Failed to retrieve data for roll number {roll_number}')

# Save data_array as JSON file
with open('data.json', 'w') as file:
    json.dump(data_array, file, indent=4)

print('Data saved as data.json')