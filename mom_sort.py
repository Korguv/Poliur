import csv


with open('mom_sort_file_1.csv', 'r', newline='',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        print(', '.join(row))

