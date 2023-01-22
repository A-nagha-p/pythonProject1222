import csv
with open('dep.csv', 'r') as original_file:
    reader = csv.reader(original_file)

    with open('new.csv', 'w', newline='') as new_file:
        writer = csv.writer(new_file)

        for i in range(5):
            writer.writerow(next(reader))

    with open('new.csv', 'r') as new_file:
        reader = csv.reader(new_file)
        for row in reader:
            print(row)