# -*- coding: utf-8 -*-
import csv
import os

MAX_LINE = 300
TITLE_COLUMN = 1
IMAGE_COLUMNS = [8, 9, 10]

seen = set()
duplicates = set()

def write_to_csv(data, index):
    with open("products_fixed_" + str(index) + ".csv", "w", newline="", encoding="utf-8-sig") as f2:
        writer = csv.writer(f2)
        writer.writerows(data)

def write_duplicate_csv(dups):
    with open("duplicates.csv", "w", newline="", encoding="utf-8-sig") as f_dup:
        for dup in dups:
            f_dup.write(dup + "\n")

with open("products_fixed.csv", "r", encoding='utf-8-sig', newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    data = []
    index = 0

    # print 300 items each csv file
    for i, row in enumerate(reader):
        if row[TITLE_COLUMN] not in seen:
            seen.add(row[TITLE_COLUMN])
            data.append(row)
            index = i
            if len(data) % MAX_LINE == 0:
                write_to_csv([header] + data, i + 1)
                data = []
        else:
            if row[TITLE_COLUMN] not in duplicates:
                duplicates.add(row[TITLE_COLUMN])
            for col in IMAGE_COLUMNS:
                if row[col] and os.path.isfile('images/' + row[col]):
                    os.remove('images/' + row[col])

    # print the rest items
    if len(data) >= 1:
        write_to_csv([header] + data, index + 1)

    write_duplicate_csv(duplicates)