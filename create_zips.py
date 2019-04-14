# -*- coding: utf-8 -*-
import csv
import os
import glob
import re
import shutil

IMAGE_COLUMNS = [8, 9, 10]
FINAL_ZIP = 'zip_all'

files = [os.path.basename(x) for x in glob.glob('./products_fixed_*.csv')]
if not os.path.exists(FINAL_ZIP):
    os.makedirs(FINAL_ZIP)

for file in files:
    zip_name = re.findall('\d+', file)[0]

    # create a folder and move images into it
    with open(file, "r", encoding='utf-8-sig', newline="") as f:
        reader = csv.reader(f)
        header = next(reader)

        if not os.path.exists(zip_name):
            os.makedirs(zip_name)

        for row in reader:
            for col in IMAGE_COLUMNS:
                if not row[col]:
                    continue
                if os.path.isfile('images/' + row[col]):
                    os.rename('images/' + row[col], zip_name + '/' + row[col])
                else:
                    print('画像が存在しない：' + row[col])

    # move csv file into the folder
    os.rename(file, zip_name + '/' + file)

    # make zip file
    shutil.make_archive(FINAL_ZIP + '/zip_' + zip_name, 'zip', zip_name)
    try:
        shutil.rmtree(zip_name)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))

shutil.make_archive(FINAL_ZIP, 'zip', FINAL_ZIP)
try:
    shutil.rmtree(FINAL_ZIP)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

