import csv
j=0
filename = 'diff.csv'
with open(filename,encoding="utf-8") as f:
 with open('train_lack.csv','w',newline='') as f1:
    reader = csv.reader(f)
    writer = csv.writer(f1)
    for row in reader:
        for i in range(0,len(row[0])):
            if row[0][i]=='/':
               print(row[0])
               line_list = row[0][i+1:].strip('\n').split('\t')
               print(line_list)
               writer.writerow(line_list)
               j = j+1
            #print(line)
print(j)
