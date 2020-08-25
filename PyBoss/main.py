import os
import csv
import datetime
import numpy as np


file_path = os.path.join("employee_data.csv")

output_path = os.path.join("reordered_employee_data.csv")

states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(file_path, 'r') as csv_file, open(output_path, 'w') as new_csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader, None)

    csv_writer = csv.writer(new_csv_file, delimiter=',', lineterminator= "\n")

    csv_writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    for row in csv_reader:
        emp_id = row[0]
        name = row[1].split(" ")
        first_name = name[0]
        last_name = name[1]
        date = datetime.datetime.strptime(row[2], "%Y-%m-%d")
        new_date = date.strftime("%m/%d/%Y")
        SSN = f"***-**-{row[3][-4:]}"
        state = row[4]
        new_state = states[f"{state}"]

        csv_writer.writerow([emp_id, first_name, last_name, new_date, SSN, new_state])