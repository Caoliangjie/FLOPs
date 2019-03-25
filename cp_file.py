import csv
import os
import subprocess
filename = 'something-something-v1-validation.csv'
label=[]
with open(filename,encoding="utf-8") as f:
 with open('val.csv','w',newline='') as f1:
    reader = csv.reader(f)
    header_row = next(reader)
    datas = []
    writer = csv.writer(f1)
    for row in reader:
        if "Moving something and something closer to each other" in row[0]:
            for i in range(len(row[0])): 
                if row[0][i]==';':
                   label.append(row[0][:i])
    for i in label:
        cmd = 'cp -r ../20bn-something-something-v1/{} /home/sda/moving-closer-each'.format(i) 
        print(cmd)
        subprocess.call(cmd, shell=True)
        print('\n')
