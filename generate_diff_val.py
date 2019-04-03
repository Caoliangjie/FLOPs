import csv
import os
filename = 'kinetics_val.csv'
filename2 = 'butong_val.txt'
with open(filename,encoding="utf-8") as f:
 #with open(filename3,encoding='utf-8') as f3:  
  with open(filename2,'w') as f2:
    reader = csv.reader(f)
    for row in reader:
        if row[0]!='label':
              row[0]=row[0].replace(" ","_")
              print(row[0])
              f2.write(row[0]+'/'+row[1]+'.mp4')
              f2.write('\n')
