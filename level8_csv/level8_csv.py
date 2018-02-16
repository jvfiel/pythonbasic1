import csv

with open('some.csv', 'rb') as f:

    f.readline()

    reader = csv.reader(f)

    for row in reader:
        print row
