import csv
import os
filename = 'something-something-v1-validation.csv'
with open(filename,encoding="utf-8") as f:
 with open('val_up.csv','w',newline='') as f1:
    reader = csv.reader(f)
    header_row = next(reader)
    datas = []
    writer = csv.writer(f1)
    for row in reader:
        if "Moving something up" in row[0]:
            print(row[0])
            writer.writerow(row)
