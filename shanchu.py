import csv
num = 0 
out=open('lack_less.csv','w',newline='') 
with open('lack_train.csv', 'r') as csvfile:
   csv_write=csv.writer(out,dialect='excel')
   x=['label','youtube_id','time_start','time_end','split','is_cc']
   csv_write.writerow(x) 
   reader = csv.reader(csvfile) 
   for line in reader:
         num += 1 
         if num > 3963: 
            for row in reader: 
                csv_write.writerow(row)
