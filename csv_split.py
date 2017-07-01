# -*- coding: utf-8 -*-
import csv
MAX_LINE = 300
def write_to_csv(data, index):
    with open("products_fixed_" + str(index) + ".csv", "w", newline="", encoding='utf-8-sig') as f2:
        writer = csv.writer(f2)
        writer.writerows(data)


with open("products_fixed.csv", "r", encoding='utf-8-sig', newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    data = []
    index = 0

    for i, row in enumerate(reader):
        data.append(row)
        index = i
        if (i + 1) % MAX_LINE == 0:
            write_to_csv([header] + data, i + 1)
            data = []

    if len(data) >= 1:
        write_to_csv([header] + data, index + 1)