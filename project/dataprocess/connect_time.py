import csv

# Read existing data from the CSV file
existing_data = []
with open('new.csv', 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    existing_data.extend(csvreader)


for row in existing_data:
    print(row)
# Optional: Print the updated data
for row in existing_data:
    no = row[10]
    time = row[11]
    socket = row[12]
    for i in existing_data:
        if no == i[0]:
            i.append(time)
            i.append(socket)
        else:
            continue


with open('training.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(existing_data)