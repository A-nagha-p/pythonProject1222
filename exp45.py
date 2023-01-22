import csv

with open('dep.csv', 'r') as original_file:
    reader = csv.reader(original_file)


    with open('odd.csv', 'w', newline='') as odd_file:
        odd_writer = csv.writer(odd_file)


        with open('even.csv', 'w', newline='') as even_file:
            even_writer = csv.writer(even_file)


            i = 1
            for row in reader:
                if i % 2 == 1:
                    odd_writer.writerow(row)
                else:
                    even_writer.writerow(row)
                i += 1

    with open('odd.csv', 'r') as odd_file:
        reader = csv.reader(odd_file)

        print("Odd rows:")
        for row in reader:
            print(row)

    with open('even.csv', 'r') as even_file:
        reader = csv.reader(even_file)

        print("Even rows:")
        for row in reader:
            print(row)