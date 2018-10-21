# -*- coding: utf-8 -*-
import csv
import os

MAX_LINE = 300
TITLE_COLUMN = 1
IMAGE_COLUMNS = [8, 9, 10]

seen = set()
duplicates = set()

def build_duplicated_title_list(titles):
    # get duplicates from array
    for title in titles:
        if title not in seen:
            seen.add(title)
        elif title not in duplicates:
            duplicates.add(title)


def remove_duplicate(array):
    duplicated_items = [item for item in array if item[TITLE_COLUMN] in duplicates]
    for duplicated_item in duplicated_items:
        for column in IMAGE_COLUMNS:
            if duplicated_item[column]:
                image_path = "images/" + duplicated_item[column]
                if os.path.exists(image_path):
                    os.remove(image_path)

    # remove all duplicates from array
    result = [item for item in array if item[TITLE_COLUMN] not in duplicates]
    return result

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

    for i, row in enumerate(reader):
        data.append(row)
    titles = [item[TITLE_COLUMN] for item in data]
    build_duplicated_title_list(titles)
    write_duplicate_csv(duplicates)

    filtered_data = remove_duplicate(data)
    data = None

    # print 300 items each csv file
    items_to_csv = []
    for i, row in enumerate(filtered_data):
        items_to_csv.append(row)
        index = i
        if (i + 1) % MAX_LINE == 0:
            write_to_csv([header] + items_to_csv, i + 1)
            items_to_csv = []

    # print the rest items
    if len(items_to_csv) >= 1:
        write_to_csv([header] + items_to_csv, index + 1)