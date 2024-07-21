import csv

# Read existing data from the CSV file
existing_data = []
with open('attackfinal.csv', 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    existing_data.extend(csvreader)

for row in existing_data:
    print(row)
# Optional: Print the updated
count = 0
for row in existing_data:
    row.append('A')


print(count)
for row in existing_data:
    print(row)

with open('attackfinal.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(existing_data)