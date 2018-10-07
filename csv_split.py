# -*- coding: utf-8 -*-
import csv
MAX_LINE = 300
TITLE_COLUMN = 1

def remove_duplicate(array):
    titles = [item[TITLE_COLUMN] for item in array]
    seen = set()
    duplicates = set()

    # get duplicates from array
    for title in titles:
        if title not in seen:
            seen.add(title)
        else:
            duplicates.add(title)

    # remove all duplicates from array
    result = [item for item in array if item[TITLE_COLUMN] not in duplicates]
    return result

def write_to_csv(data, index):
    filtered_data = remove_duplicate(data)
    with open("products_fixed_" + str(index) + ".csv", "w", newline="", encoding='utf-8-sig') as f2:
        writer = csv.writer(f2)
        writer.writerows(filtered_data)


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