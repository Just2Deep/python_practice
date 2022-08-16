# importing, modifying and exporting csv files


# import pandas as pd


# df = pd.read_csv(r'D:\python\Practice\Intermediate\names.csv')

# print(df)

import csv

with open(r'D:\python\Practice\Intermediate\names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # print(csv_reader)
    # to skip first row
    next(csv_reader)

    for row in csv_reader:
        print(row[2])


# to write to new file

with open(r'D:\python\Practice\Intermediate\names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open(r'D:\python\Practice\Intermediate\new_names.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='|')

        for row in csv_reader:
            csv_writer.writerow(row)


# using dict reader for ordered dictionary creation.

with open(r'D:\python\Practice\Intermediate\names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for row in csv_reader:
    #     print(row)

    with open(r'D:\python\Practice\Intermediate\dict_names.csv', 'w', newline='') as new_file:

        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='|')

        csv_writer.writeheader()

        for row in csv_reader:
            csv_writer.writerow(row)
