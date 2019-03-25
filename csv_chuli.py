import csv
import os
filename = 'val_lr.csv'
#os.mknod('val.csv')
with open(filename,encoding="utf-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    datas = []
    for index,row in enumerate(reader):
        print(row[0])
        os.mknod('val{}.csv'.format(index))
        with open('val{}.csv'.format(index),'w',newline='') as f1:
             writer = csv.writer(f1)
             writer.writerow(row)
