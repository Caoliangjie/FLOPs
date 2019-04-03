import csv
import os
filename = 'kinetics_train.csv'
file2 = 'train_lack.csv'
i=0
out=open('lack_train.csv','w',newline='')      
csv_write=csv.writer(out,dialect='excel')
x=['label','youtube_id','time_start','time_end','split','is_cc']
csv_write.writerow(x)
with open(file2,encoding="utf-8") as f0:
 with open(filename,encoding="utf-8") as f:
    #spamwriter = csv.writer(csvfile)
    reader = csv.reader(f)
    reader = list(reader)
    reader0 = csv.reader(f0)
    for line in reader0:
     for line2 in reader:
            #print('l1 = ',len(str(line)[2:-2]))
            #print('l2 = ', len(str(line2[1])))
            if str(line)[2:-2]==str(line2[1]):
              print(str(line)[2:-2])  
              csv_write.writerow(line2)  
              #print(line)
